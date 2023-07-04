from flask import Flask, render_template, request
from getquiz import get_new_quiz

app = Flask(__name__)

import json

"""

# Example usage
file_path = 'file.json'
questions = read_json_file(file_path)
"""
# questions=""

@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'GET':
        quizbody = get_new_quiz()
        print(quizbody)
        questions = json.loads(quizbody)['quiz']
        file_path = "data.json"
        # Open the file in write mode
        with open(file_path, "w") as json_file:
            # Write the data to the JSON file
            json.dump(questions, json_file)
        print('written data.json')
        return render_template('quiz.html', questions=questions)
    if request.method == 'POST':
        # Process submitted answer
        score = 0
        verdict = "Keep Learning !!"
        analysis_list = []
        questions = read_quiz_data('data.json')
        for i in range(len(questions)):
            selected_choice = request.form.get(str(i))
            if selected_choice is not None and selected_choice == questions[i]['answer']:
                score += 1
            else:
                analysis_list.append({"question" : questions[i]['question'] , 
                                      "response" : get_choice(questions, i, selected_choice), 
                                      "answer": get_choice(questions, i, questions[i]['answer'])}) 
        if score == 10:
            verdict = "Well Done, Keep Learning Still !"
        return render_template('result.html', verdict=verdict, score=score, analysis_list=analysis_list, total=len(questions))

def get_choice(questions, i, op):
    return questions[i]['options'][op]

def read_quiz_data(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        return json_data

if __name__ == '__main__':
    app.run(debug=True)
