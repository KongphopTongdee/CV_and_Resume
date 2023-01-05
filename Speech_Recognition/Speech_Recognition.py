import speech_recognition as sr     # Library for convert speech to text
from gtts import gTTS               # Library for convert text to speech(woman voice)
from playsound import playsound     # Library for playing sound
from datetime import datetime

r = sr.Recognizer()     # ตัวเริ่มต้น

with sr.Microphone() as source:     # Microphone สำหรับ source บัญทึกเสียง
    playsound("signal.mp3")
    audio = r.record(source, duration=5)
    playsound("signal.mp3")

    try:
        text = r.recognize_google(audio, language="en-US")
        if "I" in text:
            text = text.replace("I", "We are")
        if "too" in text:
            text = text.replace("too", "you too")
        if text == "what time is it" :
            now = datetime.now()
            text = now.strftime("It is %H hour %M minutes %S second")
    except:
        text = "sorry"
    
    print(text)
    tts = gTTS(text, lang="en")
    tts.save("answer.mp3")
    playsound("answer.mp3")



# There 2 step 
# 1. speech to text
# 2. text to speech