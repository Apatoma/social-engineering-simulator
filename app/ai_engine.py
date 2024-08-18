import random

class AIEngine:
    def __init__(self, user_input):
        self.user_input = user_input

    def generate_response(self):
        responses = [
            "This looks like a phishing attempt!",
            "Are you sure you want to click that link?",
            "This email might not be from who you think it is."
        ]
        return random.choice(responses)
