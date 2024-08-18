from flask import render_template, request, jsonify
from app import app
from .simulator import SocialEngineeringSimulator

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        simulator = SocialEngineeringSimulator(user_input)
        response = simulator.run_simulation()
        return jsonify(response)
    return render_template('index.html')
