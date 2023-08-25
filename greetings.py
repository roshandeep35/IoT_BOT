# greeting.py

import random

class Greeter:
    def __init__(self, name):
        self.name = "Roshan"
        self.greetings = [
            f"Hello, {self.name}! How can I assist you today?",
            f"Hi, {self.name}! What can I do for you?",
            f"Good to hear from you, {self.name}! How can I help?",
            f"Hey, {self.name}! Need anything?",
            f"Welcome back, {self.name}! What can I assist you with?"
        ]

    def greet(self):
        return random.choice(self.greetings)
