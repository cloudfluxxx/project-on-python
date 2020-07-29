import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
print("Initializing JARVIS")

MASTER = "Christian"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def noAnswer():
    speak("as of now I can't do what you want me to do. Sorry")


def wishMe():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-us')
        print(f"user said: {query}")

    except Exception as e:
        speak("Please say it again.")
        noAnswer()
        closingJarvis()

    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youre@gmail.com", "password")
    server.sendmail("where to send the email", to , content)
    server.close()

def closingJarvis():
    time.sleep(4)
    speak("Is there anything I can help you with?")
    asking = takeCommand()
    if "nothing" in asking.lower() or "none" in asking.lower():
        speak(f"Okay got it {MASTER}. Thank you and have a nice day!")

    return quit()

def main():

    active = True
    while active:
        speak("Initializing Jarvis")
        wishMe()
        query = takeCommand()


        if 'wikipedia' in query.lower():
            speak("searching wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences= 3)
            print(results)
            speak(results)
            closingJarvis()

        elif 'open youtube' in query.lower():
            url = "youtube.com"
            brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe %s"
            print(f"Opening youtube.com at {brave_path}....")
            webbrowser.get(brave_path).open(url)
            closingJarvis()

        elif "open google" in query.lower():
            url = "google.com"
            brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe %s"
            print(f"Opening google.com at {brave_path}....")
            webbrowser.get(brave_path).open(url)
            closingJarvis()


        elif "play music" in query.lower():
            url = "https://open.spotify.com/playlist/2a36AMRbR0wRdm62aHabGT"
            brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe %s"
            print(f"Playing music at spotify")
            webbrowser.get(brave_path).open(url)
            closingJarvis()


        elif "play music" in query.lower():
            songs_dir = "C:\\Users\\Acer\\Music"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))
            closingJarvis()


        elif "the time" in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            strDate = datetime.datetime.now().date()
            speak(f"{MASTER} the time is {strTime} and the date is {strDate}")
            closingJarvis()


        elif "email to harry" in query.lower():
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "wheretosend@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
            closingJarvis()


        elif "open facebook" in query.lower():
            url = "facebook.com"
            brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe %s"
            webbrowser.get(brave_path).open(url)
            print("Opening the web browser...")
            print("Opening facebook.com")
            speak("Opening the web browser...")
            speak("Opening facebook.com")
            closingJarvis()


        elif "open netflix" in query.lower():
            url = "netflix.com"
            brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe %s"
            print("Opening web browser...")
            print("Opening netflix...")
            speak("Opening web browser...")
            speak("Opening netflix...")
            webbrowser.get(brave_path).open(url)
            closingJarvis()

        elif "open gmail" in query.lower():
            url = "https://mail.google.com/mail/u/0/#inbox"
            brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe %s"
            print("Opening gmail.com...")
            speak("opening gmail.com...")
            webbrowser.get(brave_path).open(url)
            closingJarvis()

        else:
            noAnswer()
            closingJarvis()


main()