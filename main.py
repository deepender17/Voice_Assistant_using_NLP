import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import random
import re

def listen_to_user():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None

def speak_to_user(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except:
        return None

def run_voice_assistant():
    speak_to_user("Hello, I'm your voice assistant.")
    text = listen_to_user()
    if text:
        if "hello" in text.lower():
            response = "Hello there!"
        elif "how are you" in text.lower():
            response = "I'm doing great, thanks for asking!"
        elif "open youtube" in text.lower():
            response = "Opening YouTube..."
            webbrowser.open("https://www.youtube.com")
        elif "open camera" in text.lower():
            response = "Opening camera..."
            os.system("start microsoft.windows.camera:")
        elif "open notepad" in text.lower():
            response = "Opening Notepad..."
            os.system("notepad")
        elif "search" in text.lower():
            query = text.lower().replace("search", "")
            response = f"Searching for '{query}' on Google..."
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif "open settings" in text.lower():
            response = "Opening Settings..."
            os.system("start ms-settings:")
        elif "joke" in text.lower():
            jokes = [
                "Why did the tomato turn red? Because it saw the salad dressing!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "Why did the cookie go to the doctor? Because it felt crumbly!",
                "Why did the bicycle fall over? Because it was two-tired!",
                "Why did the computer go to the doctor? Because it had a virus!",
            ]
            response = random.choice(jokes)
        elif "calculate" in text.lower():
            expression = re.sub("[^0-9^+^\-^*^/^(^)^.]", "", text.lower().replace("calculate", ""))
            result = evaluate_expression(expression)
            if result is not None:
                response = f"The answer is: {result}"
                print(result)
            else:
                response = "I'm sorry, I couldn't understand the expression."
        else:
            response = "I'm sorry, I didn't understand what you said."
        speak_to_user(response)

run_voice_assistant()
