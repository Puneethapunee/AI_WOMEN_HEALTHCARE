# voice_module.py

import speech_recognition as sr
import pyttsx3

# ---------------- INIT ---------------- #

recognizer = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 170)

voices = engine.getProperty('voices')

# Safe voice selection (prevents crash if voices[1] not available)
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)


# ---------------- SPEAK ---------------- #

def speak(text):
    if not text:
        return

    try:
        print("🤖 Assistant:", text)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech error:", e)


# ---------------- LISTEN ---------------- #

def listen():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")

            # reduce noise impact
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=5,              # increased for better usability
                phrase_time_limit=7     # allows slightly longer speech
            )

        text = recognizer.recognize_google(audio)
        print("🧑 User:", text)

        return text.lower()

    except sr.WaitTimeoutError:
        print("⏱️ Listening timeout")
        return ""

    except sr.UnknownValueError:
        print("❓ Could not understand audio")
        return ""

    except sr.RequestError:
        print("🌐 API unavailable")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""