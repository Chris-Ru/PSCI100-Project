from flask import Flask, render_template, url_for, request, redirect, flash, render_template_string
import numpy as np
#from flask_sqlalchemy import SQLAlchemy

#create a Flask instance
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']
popular= []

#connects default URL to a function
@app.route('/')
def home():
  return render_template('home2.html')


# List of questions
questions = [
    { "text": "The evidence is inadmissible due to a Fourth Amendment violation.", "valid": True },
    { "text": "The defendant's behavior was justified under self-defense laws.", "valid": False },
    { "text": "Eyewitness testimony is always reliable.", "valid": False },
    { "text": "The exclusionary rule prohibits the use of evidence obtained through illegal searches or seizures.", "valid": True },
    { "text": "The Miranda warning is required to be given before any interrogation of a suspect in police custody.", "valid": True },
    # Add more questions here
]

@app.route('/PSCI100/argument_game', methods=['GET', 'POST'])
def argument_game():
    responses = None
    score = 0
    num_questions = len(questions)
    if request.method == 'POST':
        responses = []
        for index, question in enumerate(questions):
            response = request.form.get(str(index+1))  # Corrected index here
            responses.append({"text": question["text"], "response": response})
            if response is not None and response.lower() == str(question["valid"]).lower():
                score += 1
    return render_template('argument_game.html', questions=questions, responses=responses, score=score, num_questions=num_questions)


# List of quiz questions
questions2 = [
    {
        "question": "Which article of the Constitution establishes the legislative branch?",
        "options": ["Article I", "Article II", "Article III", "Article IV"],
        "correct_answer": "Article I"
    },
    {
        "question": "How many amendments are there in the Bill of Rights?",
        "options": ["10", "12", "5", "27"],
        "correct_answer": "10"
    },
    {
        "question": "Which amendment guarantees freedom of speech?",
        "options": ["First Amendment", "Fourth Amendment", "Fifth Amendment", "Sixth Amendment"],
        "correct_answer": "First Amendment"
    },
    # Add more questions here
]

@app.route('/PSCI100/constitutional_quiz', methods=['GET', 'POST'])
def constitutional_quiz():
    score = 0
    if request.method == 'POST':
        for question in questions2:
            selected_answer = request.form.get(question["question"])
            if selected_answer == question["correct_answer"]:
                score += 1
    return render_template('constitutional_quiz.html', questions2=questions2, score=score, num_questions=len(questions2))


if __name__ == '__main__':
    app.run(debug=True)
