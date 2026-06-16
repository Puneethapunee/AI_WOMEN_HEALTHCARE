# modules/diet_module.py

import requests
from diet_planner.diet_logic import generate_weekly_plan


# ---------------- GET USER DATA ---------------- #

def get_user_data():
    try:
        url = "http://localhost:5000/getData"
        print(f"Fetching user data from: {url}")

        res = requests.get(url, timeout=5)

        # 🔴 Check response
        if res.status_code != 200:
            raise Exception(f"API Error: {res.status_code}")

        data = res.json()
        print("DEBUG: Raw Data from Backend =", data)

        # 🔴 Validate data
        if not data or not isinstance(data, dict):
            raise Exception("Invalid or empty data received from backend")

        # 🔥 Safe parsing (handles strings from MongoDB)
        weight = int(data.get("weight", 60))
        height = int(data.get("height", 160))
        symptoms = str(data.get("symptoms", "")).lower()

        user = {
            "weight": weight,
            "height": height,
            "hb": 11,  # default for now
            "pcos": 1 if "pcos" in symptoms else 0
        }

        print("DEBUG: Processed User Data =", user)

        return user

    except Exception as e:
        print("❌ Error fetching user data:", e)

        # 🔁 FALLBACK DATA (never crash system)
        fallback_user = {
            "weight": 60,
            "height": 160,
            "hb": 11,
            "pcos": 1
        }

        print("Using fallback user:", fallback_user)
        return fallback_user


# ---------------- GET DIET PLAN ---------------- #

def get_diet_plan():
    try:
        user = get_user_data()

        print("Generating diet plan for:", user)

        # 🔥 Call ML logic
        plan = generate_weekly_plan(user)

        print("DEBUG: Generated Plan =", plan)

        # 🔴 Validate plan
        if not plan or not isinstance(plan, dict):
            raise Exception("Diet plan is invalid")

        if len(plan.keys()) == 0:
            raise Exception("Diet plan is empty")

        return plan

    except Exception as e:
        print("❌ Diet generation error:", e)

        # 🔁 FINAL SAFE FALLBACK PLAN
        fallback_plan = {
            "Monday": {
                "Breakfast": "Oats with fruits",
                "Lunch": "Brown rice with vegetables",
                "Dinner": "Grilled chicken with salad"
            }
        }

        print("Using fallback plan:", fallback_plan)
        return fallback_plan