import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr


API_KEY = "insert your API key here"

lang='en'
exitProg = False;

openai.api_key = API_KEY

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)

                if "Jarvis" in said:
                    completion = openai.ChatCompletion.create(
                        model = "gpt-3.5-turbo", 
                        messages = [{"role": "user", "content": said}])
                    text = completion['choices'][0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="co.uk")
                    speech.save("output.mp3")
                    playsound.playsound("output.mp3")
            except Exception:
                print("Error")
            if "Jarvis shut down" in said:
                exitProg = True

        return said
    
    if exitProg:
        break

    get_audio(import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr


API_KEY = "your-api-key"

lang='en'
exitProg = False;

openai.api_key = API_KEY

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)

                if "Jarvis" in said:
                    completion = openai.ChatCompletion.create(
                        model = "gpt-3.5-turbo", 
                        messages = [{"role": "user", "content": said}])
                    text = completion['choices'][0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="")
                    speech.save("output.mp3")
                    playsound.playsound("output.mp3")
            except Exception:
                print("Error")
            if "Jarvis shut down" in said:
                exitProg = True

        return said
    if exitProg:
        break
    get_audio()
