import os
import openai
from dotenv import load_dotenv
import time
import speech_recognition as sr
import pyttsx3
import numpy as np


load_dotenv()
# print(os.getenv('OPENAI_API_KEY'))
openai.api_key = os.getenv('OPENAI_API_KEY')
model = 'gpt-3.5-turbo'


r = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
# for idx, voice in enumerate(voices):
#     print(f"Voice {idx}: {voice.name}")

voice = voices[1]
engine.setProperty('voice', voice.id)
name = "Hiteshi"
greetings = [
    f"Whats up master {name}",
    # "yeah?",
    # "Well, hello there, Master of Puns and Jokes - how's it going today?",
    # f"Ahoy there, Captain {name}! How's the ship sailing?",
    # f"Bonjour, Monsieur {name}! Comment ça va? Wait, why the hell am I speaking French?"
]


# Flag to indicate whether the program should continue listening
should_listen = True


# Listen for the wake word "hey pos"
def listen_for_wake_word(source):
    print("Listening for 'Hello Mahi'...")

    while should_listen:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            if "hello mahi" in text.lower():
                print("Wake word detected.")
                engine.say(np.random.choice(greetings))
                engine.runAndWait()
                listen_and_respond(source)
                break
        except sr.UnknownValueError:
            pass

# Listen for input and respond with OpenAI API
def listen_and_respond(source):
    print("Listening...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            if text.lower() == "stop":
                print("Stopping...")
                engine.say("Goodbye!")
                engine.runAndWait()
                return # Stop listening
                break
            if not text:
                continue
            
            # Send input to OpenAI API
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{text}"}]) 
            response_text = response.choices[0].message.content
            print(f"OpenAI response: {response_text}")

            # Speak the response
            engine.say(response_text)
            engine.runAndWait()

            # # Test text-to-speech
            # test_text = "Hello, this is a test."
            # engine.say(test_text)
            # engine.runAndWait()

            if not audio:
                listen_for_wake_word(source)
        except sr.UnknownValueError:
            time.sleep(2)
            print("Silence found, shutting up, listening...")
            listen_for_wake_word(source)
            break
            
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            engine.say(f"Could not request results; {e}")
            engine.runAndWait()
            listen_for_wake_word(source)
            break


with sr.Microphone() as source:
    listen_for_wake_word(source)

r = sr.Recognizer()
mic_list = source.list_microphone_names()

# for i, mic_name in enumerate(mic_list):
#     print(f"Microphone {i}: {mic_name}")


