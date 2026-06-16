# modules/exercise_module.py

import os
import webbrowser


def show_exercises(query=None):
    try:
        # 📁 Current directory (modules)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # ⬆ Move to parent directory (project root)
        parent_dir = os.path.abspath(os.path.join(current_dir, ".."))

        # 📄 HTML file path
        file_path = os.path.join(parent_dir, "exercise_hub.html")

        # 🔍 Debug
        print("Opening file:", file_path)

        # ❌ Check if file exists
        if not os.path.exists(file_path):
            print("❌ exercise_hub.html not found")

            # fallback → open YouTube
            webbrowser.open("https://www.youtube.com/results?search_query=pcos+exercise")
            return

        # ✅ Fix path for browser (important for Windows)
        file_path = file_path.replace("\\", "/")

        # 🌐 Open file
        webbrowser.open(f"file:///{file_path}")

    except Exception as e:
        print("❌ Error opening exercise page:", e)

        # 🔁 fallback (VERY IMPORTANT)
        webbrowser.open("https://www.youtube.com/results?search_query=pcos+exercise")