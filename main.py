from flask import Flask, render_template, url_for, request, redirect, flash, render_template_string
import numpy as np
import random
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
    { "text": "The Chief Justice of the United States is appointed for a term of 10 years.", "valid": False },
    { "text": "The United States Supreme Court has original jurisdiction in cases involving disputes between states.", "valid": True },
    { "text": "The judicial branch of the United States government has the power to interpret laws.", "valid": True },
    { "text": "The Supreme Court has the authority to impeach and remove federal judges.", "valid": False },
    { "text": "The United States Attorney General is responsible for appointing federal judges.", "valid": False },
    { "text": "Federal judges are appointed for life.", "valid": True },
    { "text": "The United States Constitution guarantees the right to a fair trial in the Sixth Amendment.", "valid": True },
    { "text": "The President of the United States has the power to pardon federal offenses.", "valid": True },
    { "text": "The Supreme Court has the authority to declare a law unconstitutional.", "valid": True },
    { "text": "The judicial branch is responsible for enforcing laws.", "valid": False },
    { "text": "The United States Supreme Court has 12 justices.", "valid": False },
    { "text": "The majority of cases heard by the Supreme Court are original jurisdiction cases.", "valid": False },
    { "text": "The Chief Justice of the United States is responsible for presiding over presidential impeachment trials.", "valid": True },
    { "text": "The Chief Justice of the United States has the authority to administer the oath of office to the President.", "valid": False },
    { "text": "The Supreme Court has the power of judicial review over both federal and state laws.", "valid": True },
    { "text": "The judicial branch of government includes both state and federal courts.", "valid": True },
    { "text": "Federal judges are elected by popular vote.", "valid": False },
    { "text": "The Supreme Court has original jurisdiction in cases involving foreign diplomats.", "valid": True },
    { "text": "Federal judges must be confirmed by the House of Representatives.", "valid": False },
    { "text": "The United States Attorney General is a member of the judicial branch.", "valid": False },
    { "text": "The President of the United States can remove federal judges from office.", "valid": False },
    { "text": "The Supreme Court has the authority to hear cases involving violations of international law.", "valid": True },
    { "text": "The United States Constitution guarantees the right to a speedy and public trial.", "valid": True },
    { "text": "The judicial branch has the power to declare executive actions unconstitutional.", "valid": True },
    { "text": "Federal judges are subject to term limits.", "valid": False },
    { "text": "The judicial branch is responsible for enforcing treaties signed by the President.", "valid": False },
    { "text": "The Supreme Court has the authority to interpret the Constitution.", "valid": True },
    { "text": "The United States Constitution grants Congress the power to impeach and remove federal judges.", "valid": True },
    { "text": "The Chief Justice of the United States is responsible for drafting executive orders.", "valid": False },
]



@app.route('/argument_game', methods=['GET', 'POST'])
def argument_game():
    score = 0
    random_questions = random.sample(questions, 10)  # Randomly select 10 questions

    if request.method == 'POST':
        responses = []
        for index, question in enumerate(random_questions):
            response = request.form.get(str(index+1))  # Corrected index here
            responses.append({"text": question["text"], "response": response})
            if response is not None and response.lower() == str(question["valid"]).lower():
                score += 1
    else:
        responses = None

    return render_template('argument_game.html', questions=random_questions, responses=responses, score=score, size=len(random_questions))


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
    {
        "question": "What does the First Amendment to the United States Constitution protect?",
        "options": ["Freedom of speech", "Freedom of religion", "Freedom of the press", "All of the above"],
        "correct_answer": "All of the above"
    },
    {
        "question": "Who has the power to declare war according to the United States Constitution?",
        "options": ["The President", "The Congress", "The Supreme Court", "The State Governors"],
        "correct_answer": "The Congress"
    },
    {
        "question": "What is the term length for a United States Senator?",
        "options": ["2 years", "4 years", "6 years", "8 years"],
        "correct_answer": "6 years"
    },
    {
        "question": "Which branch of government is responsible for interpreting laws?",
        "options": ["Legislative", "Executive", "Judicial", "Administrative"],
        "correct_answer": "Judicial"
    },
    {
        "question": "Who is the Commander-in-Chief of the United States military?",
        "options": ["The President", "The Secretary of Defense", "The Vice President", "The Speaker of the House"],
        "correct_answer": "The President"
    },
    {
        "question": "What is the purpose of the Electoral College?",
        "options": ["To elect the President and Vice President", "To elect Senators", "To elect Governors", "To elect Mayors"],
        "correct_answer": "To elect the President and Vice President"
    },
    {
        "question": "Which amendment guarantees the right to a fair trial?",
        "options": ["First Amendment", "Fifth Amendment", "Sixth Amendment", "Eighth Amendment"],
        "correct_answer": "Sixth Amendment"
    },
    {
        "question": "What is the term length for a President of the United States?",
        "options": ["2 years", "4 years", "6 years", "8 years"],
        "correct_answer": "4 years"
    },
    {
        "question": "Who has the power to veto legislation passed by Congress?",
        "options": ["The President", "The Supreme Court", "The Speaker of the House", "The Senate Majority Leader"],
        "correct_answer": "The President"
    }
    # Add more questions here
]

@app.route('/constitutional_quiz', methods=['GET', 'POST'])
def constitutional_quiz():
    score = 0
    random_questions2 = random.sample(questions2, 10)  # Randomly select 10 questions

    if request.method == 'POST':
        responses = []
        for index, question in enumerate(random_questions2):
            response = request.form.get(question["question"])  # Corrected index here
            print(response)
            responses.append({"text": question["question"], "response": response})
            if response is not None and response.lower() == str(question["correct_answer"]).lower():
                score += 1
    else:
        responses = None

    return render_template('constitutional_quiz.html', questions2=random_questions2, responses=responses, score=score, size=len(random_questions2))

@app.route('/jeopardy', methods=['GET', 'POST'])
def jeopardy():
    return render_template('jeopardy.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
