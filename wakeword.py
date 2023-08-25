# wake_word_detector.py

import speech_recognition as sr
from greetings import Greeter

class WakeWordDetector:
    def __init__(self, wake_word, name):
        self.wake_word = wake_word
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.greeter = Greeter(name)
        self.stopped = False
        self.paused = False

    def listen_for_wake_word(self):
        with self.microphone as source:
            print("Listening for the wake word...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                # if stop or pause command is detected, stop or pause listening
                if 'stop' in text.lower():
                    self.stopped = True
                    return
                if 'pause' in text.lower():
                    self.paused = True
                    return
                
                if self.wake_word in text.lower():
                    # if there is additional text after the wake word, return it as a command
                    if len(text.lower().split(self.wake_word)) > 3 and text.lower().split(self.wake_word)[1].strip() != "":
                        command = text.lower().replace(self.wake_word, '').strip()
                        return command
                    else:
                        print(self.greeter.greet())
                        return True
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
