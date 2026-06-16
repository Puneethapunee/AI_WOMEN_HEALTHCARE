from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from diet_planner.diet_logic import (
    generate_weekly_plan,
    generate_monthly_plan,
    generate_yearly_plan
)

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

import requests   # ✅ ADDED

app = FastAPI()


# ---------------- BMI ----------------
def calculate_bmi(weight, height):
    h = height / 100
    return round(weight / (h * h), 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# ---------------- PDF GENERATION ----------------
def create_pdf(plan, filename="diet_plan.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    wrap_style = styles["BodyText"]
    wrap_style.wordWrap = "CJK"

    content = []

    content.append(Paragraph("AI Diet Plan - FemAI Care", styles["Title"]))
    content.append(Spacer(1, 12))

    for day, meals in plan.items():

        content.append(Paragraph(day, styles["Heading2"]))

        table_data = [["Meal Type", "Food Items"]]

        if isinstance(meals, dict):
            for meal, foods in meals.items():

                if isinstance(foods, list):
                    food_text = "<br/>".join([f"• {f}" for f in foods])
                else:
                    food_text = str(foods)

                meal_para = Paragraph(str(meal), wrap_style)
                food_para = Paragraph(food_text, wrap_style)

                table_data.append([meal_para, food_para])

        table = Table(table_data, colWidths=[130, 370], repeatRows=1)

        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e91e63")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
        ]))

        content.append(table)
        content.append(Spacer(1, 15))

    doc.build(content)


# ---------------- HOME ----------------
@app.get("/", response_class=HTMLResponse)
def home():
    return "<h2>Diet Planner Running</h2>"


# ---------------- GENERATE (FORM BASED) ----------------
@app.post("/generate", response_class=HTMLResponse)
def generate(
    age: int = Form(...),
    weight: float = Form(...),
    height: float = Form(...),
    pcos: int = Form(...),
    hb: float = Form(...),
    plan_type: str = Form(...)
):

    user = {
        "age": age,
        "weight": weight,
        "height": height,
        "pcos": pcos,
        "hb": hb
    }

    if plan_type == "weekly":
        plan = generate_weekly_plan(user)
    elif plan_type == "monthly":
        plan = generate_monthly_plan(user)
    else:
        plan = generate_yearly_plan(user)

    create_pdf(plan)

    return "<h3>Diet generated. Download PDF below.</h3><a href='/download'>Download</a>"


# ---------------- 🔥 NEW AUTO API (IMPORTANT) ----------------
@app.get("/generate_auto")
def generate_auto():
    try:
        # 🔥 fetch user data from Node backend
        res = requests.get("http://localhost:5000/getData")
        data = res.json()

        user = {
            "age": int(data["age"]),
            "weight": float(data["weight"]),
            "height": float(data["height"]),
            "pcos": 1 if "pcos" in data["symptoms"].lower() else 0,
            "hb": 11
        }

        plan = generate_weekly_plan(user)

        return plan

    except Exception as e:
        return {"error": str(e)}


# ---------------- DOWNLOAD ----------------
@app.get("/download")
def download():
    return FileResponse("diet_plan.pdf", media_type="application/pdf", filename="diet_plan.pdf")