import pyttsx3
from datetime import date,datetime
import speech_recognition as sr
import webbrowser as wb
bot = pyttsx3.init()
voice = bot.getProperty('voices')
bot.setProperty('voice',voice[1].id)

def speak(audio):
    print("BOT: "+audio)
    bot.say(audio)
    bot.runAndWait()
def time():
    Time = datetime.now().strftime("%H hours %M minutes %S seconds")
    speak(Time)
def welcome():
    hour = datetime.now().hour
    if hour >= 0 and hour <12:
        speak("Good morning Hung")
    elif hour >=12  and hour <18:
        speak("Good afternoon Hung") 
    elif hour >= 18 and hour <=24:
        speak("Good night Hung")
    speak("How can i help you sir?")
def command():
    cmd = sr.Recognizer()
    with sr.Microphone() as mic:
        sr.Recognizer().adjust_for_ambient_noise(mic)
        speak("I'm listening")
        cmd.pause_threshold = 5 #dung 2 giay truoc khi nghe lenh moi
        audio = cmd.listen(mic)
    speak("...")
    try:
        query = cmd.recognize_google(audio,language='en')
        print("YOU: "+query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input('Your order is: '))
    return query
if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if 'google' in query:
            speak("What should i search boss?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if 'youtube' in query:
            speak("What should i search boss?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif 'today' in query:
            today = date.today().strftime("%B %d, %Y")
            speak(today)
        elif 'time' in query:
            time()
        elif 'bye' in query:
            speak("Good bye boss")
            quit()
        else:
            speak("I'm fine thank you and you")