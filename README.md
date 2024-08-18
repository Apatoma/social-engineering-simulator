Social Engineering Simulator

This is a basic Social Engineering Simulator designed for ethical hacking purposes. The application uses AI to simulate social engineering attacks, such as phishing attempts, to train users in recognizing and responding to such threats.
Project Structure

plaintext

social-engineering-simulator/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── ai_engine.py
│   ├── simulator.py
│   ├── config.py
│   └── utils.py
├── templates/
│   └── index.html
├── tests/
│   ├── __init__.py
│   ├── test_ai_engine.py
│   ├── test_simulator.py
│   ├── test_utils.py
│   └── test_models.py
├── requirements.txt
├── README.md
└── setup.py

Installation

    Clone the Repository:

    bash

git clone https://github.com/Apatoma/social-engineering-simulator.git
cd social-engineering-simulator

Create a Virtual Environment (Optional but Recommended):

bash

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:

bash

pip install -r requirements.txt

Run the Application:

bash

    python -m flask run

    The application should now be running at http://127.0.0.1:5000/.

Usage

    Open the application in your web browser.
    Enter any text that might represent a suspicious message or potential phishing content.
    The AI will simulate a social engineering response based on the input provided.

Running Tests

You can run the unit tests to ensure that everything is working correctly:

bash

python -m unittest discover tests

This command will automatically discover and run all tests in the tests/ directory.
Expanding the Project

This project is designed as a starting point for a more complex social engineering simulator. Here are a few ideas for expanding it:

    Enhanced AI: Integrate more sophisticated AI models for analyzing and generating social engineering attacks using Natural Language Processing (NLP) techniques.
    User Management: Implement a database to store user interactions, simulate attacks on a per-user basis, and provide detailed reports on user vulnerabilities.
    Real-World Integration: Add email or messaging API integration to simulate real-world phishing attempts in a controlled environment.
    Custom Scenarios: Allow administrators to create custom scenarios for training purposes, adjusting the difficulty and nature of the simulated attacks.

Contributing

Contributions are welcome! If you'd like to improve the project, feel free to submit a pull request or open an issue for discussion.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
Disclaimer

This tool is intended for educational and ethical hacking purposes only. It should only be used in environments where you have explicit permission to test and simulate attacks. Misuse of this tool can result in legal consequences.
