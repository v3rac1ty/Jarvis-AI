import speech_recognition as sr
import pyttsx3
import openai

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            print("Sorry, an error occurred while processing your request. Please try again later.")
        return ""

# Function to generate voice response using GPT model
def generate_voice_response(input_text):
    response = openai.Completion.create(
        engine='davinci',
        prompt=input_text,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Function to convert text to speech
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Main program loop
while True:
    # Take voice input
    input_text = speech_to_text()

    # Generate voice response
    response_text = generate_voice_response(input_text)

    # Convert response text to speech
    text_to_speech(response_text)
