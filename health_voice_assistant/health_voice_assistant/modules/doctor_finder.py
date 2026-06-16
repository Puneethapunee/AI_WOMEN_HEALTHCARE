# modules/doctor_finder.py

import os
import webbrowser


# ---------------- COMMON FUNCTION ---------------- #

def open_html_file(filename, fallback_url=None):
    try:
        # 📁 Get project root
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.abspath(os.path.join(current_dir, ".."))

        file_path = os.path.join(parent_dir, filename)

        print("Opening:", file_path)

        # ❌ Check if file exists
        if not os.path.exists(file_path):
            print(f"❌ {filename} not found")

            if fallback_url:
                webbrowser.open(fallback_url)
            return

        # ✅ Fix path for browser
        file_path = file_path.replace("\\", "/")

        webbrowser.open(f"file:///{file_path}")

    except Exception as e:
        print("❌ Error:", e)

        # 🔁 fallback
        if fallback_url:
            webbrowser.open(fallback_url)


# ---------------- FEATURES ---------------- #

def open_doctors():
    open_html_file(
        "find_doctors.html",
        fallback_url="https://www.google.com/maps/search/gynecologist+near+me"
    )


def open_appointment():
    open_html_file(
        "doctor_appointment.html",
        fallback_url="https://www.practo.com/"
    )


def open_lab():
    open_html_file(
        "blood_sample.html",
        fallback_url="https://www.lalpathlabs.com/"
    )