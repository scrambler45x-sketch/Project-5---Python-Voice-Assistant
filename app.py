from flask import Flask, render_template
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
import pyautogui
import pyjokes

from weather import get_weather

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

engine = pyttsx3.init()
engine.setProperty("rate", 170)



def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print("You:", command)
            return command

        except:
            return ""



def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")


def tell_date():
    today = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today is {today}")


def calculator(command):
    expression = command.replace("calculate", "")
    expression = expression.replace("plus", "+")
    expression = expression.replace("minus", "-")
    expression = expression.replace("times", "*")
    expression = expression.replace("multiplied by", "*")
    expression = expression.replace("divided by", "/")

    try:
        answer = eval(expression)
        speak(f"The answer is {answer}")
    except:
        speak("Unable to calculate.")


def create_note():
    speak("What should I write?")

    text = listen()

    if text:
        with open("notes.txt", "a") as file:
            file.write(text + "\n")

        speak("Note saved.")


def open_application(command):

    if "notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")

    elif "calculator" in command:
        os.system("calc")
        speak("Opening Calculator")

    elif "chrome" in command:
        os.system("start chrome")
        speak("Opening Chrome")

    else:
        speak("Application not available.")


def open_folder(command):

    home = os.path.expanduser("~")

    folders = {
        "desktop": "Desktop",
        "downloads": "Downloads",
        "documents": "Documents",
        "pictures": "Pictures"
    }

    for key in folders:

        if key in command:
            os.startfile(os.path.join(home, folders[key]))
            speak(f"Opening {key}")
            return

    speak("Folder not found.")


def open_site(command):

    websites = {
        "google": "https://google.com",
        "youtube": "https://youtube.com",
        "github": "https://github.com",
        "gmail": "https://mail.google.com"
    }

    for name in websites:

        if name in command:
            webbrowser.open(websites[name])
            speak(f"Opening {name}")
            return


def google_search(command):

    query = command.replace("search google for", "").strip()

    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )

    speak("Searching Google")


def play_music():

    folder = input("Enter music folder path: ")

    if os.path.exists(folder):

        songs = os.listdir(folder)

        if songs:
            music = random.choice(songs)
            os.startfile(os.path.join(folder, music))
            speak("Playing music")

        else:
            speak("No songs found.")

    else:
        speak("Folder does not exist.")


def take_screenshot():

    if not os.path.exists("screenshots"):
        os.mkdir("screenshots")

    filename = datetime.datetime.now().strftime("%H%M%S") + ".png"

    image = pyautogui.screenshot()
    image.save(os.path.join("screenshots", filename))

    speak("Screenshot saved.")


def tell_joke():
    speak(pyjokes.get_joke())


def weather(command):

    city = command.replace("weather in", "").strip()

    if city == "":
        speak("Please tell the city name.")
        return

    message = get_weather(city)
    speak(message)


def greet():

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning!")

    elif hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Welcome to Python Voice Assistant.")



def execute_command(command):

    if command == "":
        return "No command detected."

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "weather" in command:
        weather(command)

    elif "calculate" in command:
        calculator(command)

    elif "note" in command:
        create_note()

    elif "search google for" in command:
        google_search(command)

    elif "open google" in command:
        open_site(command)

    elif "open youtube" in command:
        open_site(command)

    elif "open github" in command:
        open_site(command)

    elif "open gmail" in command:
        open_site(command)

    elif "music" in command:
        play_music()

    elif "screenshot" in command:
        take_screenshot()

    elif "joke" in command:
        tell_joke()

    elif any(x in command for x in
             ["notepad", "calculator", "chrome"]):
        open_application(command)

    elif any(x in command for x in
             ["desktop", "downloads",
              "documents", "pictures"]):
        open_folder(command)

    elif command in ["bye", "exit", "stop", "goodbye"]:
        speak("Goodbye!")
        return "Goodbye!"

    else:
        speak("Sorry, I don't understand.")

    return command


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/listen")
def assistant():

    greet()

    command = listen()

    result = execute_command(command)

    return result


if __name__ == "__main__":

    if not os.path.exists("screenshots"):
        os.mkdir("screenshots")

    if not os.path.exists("notes.txt"):
        open("notes.txt", "w").close()

    app.run(debug=True)
