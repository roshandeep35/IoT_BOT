# command_processor.py

import speech_recognition as sr
import openai
from dotenv import load_dotenv
import os
load_dotenv()

class CommandProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_for_command(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                return self.process_command(command)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                return False
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return False
            
            
    def process_command(self, command):

         # Send input to OpenAI API
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{command}"}]) 
        response_text = response.choices[0].message.content
        print(f"OpenAI response: {response_text}")
        return response_text
        # return response.choices[0].text.strip()
