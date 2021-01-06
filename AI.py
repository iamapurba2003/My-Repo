import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib
import os
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=7 and hour<12:
        speak("Good Morning Sir!")
        print("Good Morning Sir!")

    if hour>=12 and hour<17:
        speak("Good Afternoon Sir!")
        print("Good Afternoon Sir!")

    if hour>=17 and hour<20:
        speak("Good Evening Sir!")
        print("Good Evening Sir!")
    
    if hour>=20 and hour<0:
        speak("Good Night Sir!")
        print("Good Night Sir!")
    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.login('dehimangshu03@gmail.com', 'password#$34')
     server.sendmail('dehimangshu03@gmail.com', to, content)
     server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            os.startfile("https://www.youtube.com")

        elif 'open google' in query:
            os.startfile("https://www.google.com")

        elif 'open stackoverflow' in query:
            os.startfile("https://www.stackoverflow.com")
        
        elif 'open github' in query:
            os.startfile("https://www.github.com")

        elif 'open gfg' in query or 'open geeks for geeks' in query:
            os.startfile("https://www.geeksforgeeks.org")

        elif 'open w3schools' in query:
            os.startfile("https://www.w3schools.com")
        
        elif 'open Chrome' in query:
            os.startfile("Chrome.exe")
            
        elif 'play music' in query:
            mdir = 'D:\Alan Walker x David Whistle - Routine.mp3'
            os.startfile(mdir)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "Code.exe"
            os.startfile(codePath)

        elif 'Send an Email' in query:
            try:
                to = input("Please enter the recipient's address: ")    
                speak("What should I convey?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception:
                speak("Sorry, email was not sent due to some potential errors")    

        elif 'Send an individual WhatsApp' in query:
            speak("Enter receiver's number along with the dialling code and plus symbol")
            num_input = input("Enter receiver's number: ")
            speak("What should I send?")
            print("What should I send?")
            msg = input()
            speak("Enter time unit in hour format: ")
            print("Enter time unit in hour format: ")
            time_hr = input()
            speak("Enter time unit in minute format: ")
            print("Enter time unit in minute format: ")
            time_min = input()
            speak("Set delay in seconds")
            print("Set delay in seconds: ")
            setDelay = input()
            kit.sendwhatmsg(num_input, msg, time_hr, time_min, setDelay)
        elif 'Quit' in query:
            break
            exit()































































