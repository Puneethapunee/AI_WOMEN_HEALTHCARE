# intent_classifier.py

def classify_intent(query):
    if not query:
        return "unknown"

    query = query.lower()

    # 🔥 DIET
    if any(word in query for word in [
        "diet", "food", "eat", "meal", "nutrition", "what should i eat"
    ]):
        return "diet"

    # 🔥 EXERCISE
    elif any(word in query for word in [
        "exercise", "workout", "fitness", "training", "yoga"
    ]):
        return "exercise"

    # 🔥 DOCTOR
    elif any(word in query for word in [
        "doctor", "gynecologist", "hospital", "clinic"
    ]):
        return "doctor"

    # 🔥 APPOINTMENT
    elif any(word in query for word in [
        "appointment", "book", "schedule", "reminder"
    ]):
        return "appointment"

    # 🔥 LAB / TESTS
    elif any(word in query for word in [
        "blood", "test", "lab", "scan", "checkup"
    ]):
        return "lab"

    # 🔴 STOP
    elif any(word in query for word in [
        "stop", "exit", "quit"
    ]):
        return "stop"

    # 🔥 GENERAL PCOS QUESTIONS
    elif any(word in query for word in [
        "pcos", "pcod", "symptoms", "weight", "periods"
    ]):
        return "general"

    # ❓ UNKNOWN
    else:
        return "unknown"