# main_controller.py

from modules.intent_classifier import classify_intent
from modules.doctor_finder import open_doctors, open_appointment, open_lab
from modules.exercise_module import show_exercises
from modules.diet_module import get_diet_plan
from ai_module import get_ai_response

from voice_module import listen, speak


# ---------------- PROCESS QUERY ---------------- #

def process_query(text, user=None):
    text = text.lower()

    try:
        intent = classify_intent(text)
        print("Detected intent:", intent)

        # 🔥 EXERCISE
        if intent == "exercise":
            show_exercises(text)
            return "Opening exercise videos for PCOS."

        # 🔥 DIET
        elif intent == "diet":
            plan = get_diet_plan()

            if not plan or not isinstance(plan, dict):
                return "Sorry, I could not generate a diet plan right now."

            first_day = list(plan.keys())[0]
            meals = plan[first_day]

            response = f"Here is your diet plan for {first_day}. "

            for meal, item in meals.items():
                response += f"{meal}: {item}. "

            return response

        # 🔥 DOCTOR
        elif intent == "doctor":
            open_doctors()
            return "Showing doctors near you."

        # 🔥 APPOINTMENT
        elif intent == "appointment":
            open_appointment()
            return "Opening appointment system."

        # 🔥 LAB
        elif intent == "lab":
            open_lab()
            return "Opening lab services."

        # 🔴 STOP handled in main loop
        elif intent == "stop":
            return "Stopping assistant."

        # 🤖 AI RESPONSE (NEW DEFAULT)
        else:
            return get_ai_response(text)

    except Exception as e:
        print("Error:", e)
        return "Something went wrong. Please try again."


# ---------------- MAIN LOOP ---------------- #

def run_assistant():
    print("Voice Assistant Started...")

    speak("Hello, your health assistant is ready.")

    while True:
        text = listen()

        if not text:
            continue

        print("You said:", text)

        # 🔴 STOP COMMAND
        if any(word in text for word in ["stop", "exit", "quit"]):
            speak("Stopping assistant.")
            print("Assistant stopped.")
            break

        # 🧠 PROCESS
        response = process_query(text)

        if not response:
            response = "Sorry, I didn't catch that."

        print("Assistant:", response)
        speak(response)


# ---------------- START ---------------- #

if __name__ == "__main__":
    run_assistant()