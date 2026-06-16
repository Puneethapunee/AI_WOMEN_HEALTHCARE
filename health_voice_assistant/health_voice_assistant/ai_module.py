# ai_module.py (OFFLINE VERSION)

def get_ai_response(text):
    text = text.lower()

    # 🔥 PCOS KNOWLEDGE
    if "pcos" in text and "what" in text:
        return "PCOS is a hormonal condition that affects women. It can cause irregular periods, weight gain, acne, and difficulty in ovulation."

    elif "symptoms" in text:
        return "Common symptoms of PCOS include irregular periods, acne, hair growth, and weight gain."

    elif "cure" in text:
        return "PCOS cannot be completely cured, but it can be managed with diet, exercise, and proper medical care."

    elif "weight" in text:
        return "Weight can be managed through regular exercise, healthy eating, and avoiding processed foods."

    elif "period" in text:
        return "Irregular periods are a common symptom of PCOS. Maintaining a healthy lifestyle can help regulate them."

    # 🔥 GENERAL HEALTH
    elif "hello" in text or "hi" in text:
        return "Hello! I am your health assistant. How can I help you?"

    elif "thank" in text:
        return "You're welcome! Take care of your health."

    # 🔥 FALLBACK
    else:
        return "I can help you with PCOS, diet, exercise, and doctor recommendations."