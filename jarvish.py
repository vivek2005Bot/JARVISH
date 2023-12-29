import pyttsx3
import speech_recognition as sr

def speak(text):
  engine=pyttsx3.init()
  ID='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
  voices=engine.setProperty('voice',ID)
  print("")
  print(f"==> jarvish : {text}")
  print("")
  engine.say(text=text)
  engine.runAndWait()

def speachrecognizer():
  r=sr.Recognizer()
  with sr.Microphone() as source:
     print("Listening...")
     r.pause_threshold=1
     audio=r.listen(source,0,8)
  
  try:
    print("recognizing.......")
    query=r.recognize_google(audio,language="en")
    print(f"==> vivek : {query}")
    return query.lower()
  
  except:
    return ""


def MainExicution(query):
  Query=str(query).lower()

  if "hello" in Query:
    speak("Hello sir , Welcome back")
  elif "bye" in Query:
    speak("Nice to meet you sir,Have a nice day")
  elif "time" in Query:
    from datetime import datetime
    time=datetime.now().strftime("%H:%M")
    speak(f"The time now is: {time}")
  

while True:
  Query=speachrecognizer()
  MainExicution(Query)