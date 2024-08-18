from .ai_engine.py import AIEngine

class SocialEngineeringSimulator:
    def __init__(self, user_input):
        self.user_input = user_input
        self.ai_engine = AIEngine(user_input)

    def run_simulation(self):
        response = self.ai_engine.generate_response()
        return {"response": response}
