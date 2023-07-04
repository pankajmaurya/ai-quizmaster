from flask import Flask, render_template, request

app = Flask(__name__)

import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        return json_data

# Example usage
file_path = 'file.json'
questions = read_json_file(file_path)

@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Process submitted answer
        score = 0
        for i in range(len(questions)):
            selected_choice = request.form.get(str(i))
            if selected_choice is not None and selected_choice == questions[i]['answer']:
                score += 1
        return render_template('result.html', score=score, total=len(questions))
    return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
