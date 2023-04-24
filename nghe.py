import speech_recognition
robot_ear=speech_recognition.Recognizer() #khởi tạo cái có thể nghe
with speech_recognition.Microphone() as mic: #bật mic và dùng xong r sẽ tắt
    print("Robot: I'm Listening")
    audio = robot_ear.listen(mic)
try:
    you = robot_ear.recognize_google(audio)
except:
    you=""
print("you: "+you)