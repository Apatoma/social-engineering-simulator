import unittest
from app.simulator import SocialEngineeringSimulator

class TestSocialEngineeringSimulator(unittest.TestCase):
    def test_run_simulation(self):
        simulator = SocialEngineeringSimulator("Test input")
        response = simulator.run_simulation()
        self.assertIn("response", response)
        self.assertIn(response["response"], [
            "This looks like a phishing attempt!",
            "Are you sure you want to click that link?",
            "This email might not be from who you think it is."
        ])

if __name__ == '__main__':
    unittest.main()
