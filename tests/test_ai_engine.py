import unittest
from app.ai_engine import AIEngine

class TestAIEngine(unittest.TestCase):
    def test_generate_response(self):
        engine = AIEngine("Test input")
        response = engine.generate_response()
        self.assertIn(response, [
            "This looks like a phishing attempt!",
            "Are you sure you want to click that link?",
            "This email might not be from who you think it is."
        ])

if __name__ == '__main__':
    unittest.main()
