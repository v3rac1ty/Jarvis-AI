import os
import openai
import speech_recognition as sr
from gtts import gTTS
import playsound
import requests

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

if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    gpt_client = GPTClient()
    tts = TTSEngine()
    net_query = InternetQuery()

    while True:
        user_input = recognizer.recognize_speech()

        if user_input:
            gpt_input = f"You said: {user_input}"
            gpt_response = gpt_client.generate_response(gpt_input)
            print("Jarvis:", gpt_response)
            tts.speak(gpt_response)

            if "search" in user_input.lower():
                query = user_input.lower().replace("search", "").strip()
                search_result = net_query.search(query)
                print("Search Result:", search_result)
                tts.speak(search_result)
