import speech_recognition
import pyttsx3
from datetime import date,datetime #thư viện ngày, giờ
robot_ear=speech_recognition.Recognizer() #khởi tạo cái có thể nghe
robot_mouth = pyttsx3.init() #miệng robot
robot_brain = ""
while True:
    with speech_recognition.Microphone() as mic: #bật mic và dùng xong r sẽ tắt
        robot_ear.adjust_for_ambient_noise(mic)
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you=""
    print("you: "+you)
    if you == '':
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Hưng"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif'stupid' in you:
        robot_brain = "exactly"
    elif 'bye' in you:
        robot_brain = "Bye BossHung"
        print(robot_brain)
        robot_mouth.say("Robot: "+robot_brain)
        robot_mouth.runAndWait() 
        break
    else:
        robot_brain = "I'm fine thank you and you"
    print(robot_brain)
    robot_mouth.say("Robot: "+robot_brain)
    robot_mouth.runAndWait()    