import os
import openai
import speech_recognition as sr
from gtts import gTTS
import playsound
import requests
import tkinter as tk
from tkinter import scrolledtext

# Set your OpenAI GPT-3.5 API key
openai.api_key = os.environ["OPENAI"]

class SpeechRecognizer:
    def recognize_speech(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something:")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

class GPTClient:
    def generate_response(self, prompt):
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.7,
            max_tokens=500,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()

class TTSEngine:
    def speak(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save('output.mp3')
        playsound.playsound('output.mp3')
        os.remove('output.mp3')

class InternetQuery:
    def search(self, query):
        base_url = "https://api.duckduckgo.com/"
        params = {'q': query, 'format': 'json'}
        response = requests.get(base_url, params=params)
        data = response.json()
        if 'Abstract' in data:
            return data['Abstract']
        else:
            return "No information found."

class JarvisGUI:
    def __init__(self, root, recognizer, gpt, tts, net_query):
        self.root = root
        self.recognizer = recognizer
        self.gpt = gpt
        self.tts = tts
        self.net_query = net_query

        self.root.title("Jarvis GUI")
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15)
        self.text_area.pack(padx=10, pady=10)

        speak_button = tk.Button(root, text="Speak", command=self.run_jarvis)
        speak_button.pack(pady=5)

    def run_jarvis(self):
        user_input = self.recognizer.recognize_speech()
        if not user_input:
            return
        gpt_input = f"You said: {user_input}"
        gpt_response = self.gpt.generate_response(gpt_input)
        self.text_area.insert(tk.END, f"You: {user_input}\nJarvis: {gpt_response}\n\n")
        self.tts.speak(gpt_response)
        if "search" in user_input.lower():
            query = user_input.lower().replace("search", "").strip()
            search_result = self.net_query.search(query)
            self.text_area.insert(tk.END, f"Search Result: {search_result}\n\n")
            self.tts.speak(search_result)

if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    gpt_client = GPTClient()
    tts = TTSEngine()
    net_query = InternetQuery()

    root = tk.Tk()
    gui = JarvisGUI(root, recognizer, gpt_client, tts, net_query)
    root.mainloop()
