import projects
from flask import Flask, render_template, url_for, request, redirect, flash, render_template_string
import numpy as np
#from flask_sqlalchemy import SQLAlchemy

#create a Flask instance
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']
popular= []

#connects default URL to a function
@app.route('/', methods=['GET','POST'])
def home():
  if(request.method == 'POST'):
    form = request.form
    product = form['product']  
    open("products.txt", "a").write("\n" + product)
    a = open("products.txt", "r").read()
    popular = a.split("\n")
    if(len(popular) > 7):
      popular.pop(0)
      seperator = '\n'
      newContent = seperator.join(popular)
      open("products.txt", "w").write(newContent)
    return redirect("https://www.amazon.com/s?k=" + product +"&ref=nb_sb_noss")
  a = open("products.txt", "r").read()
  popular = a.split("\n")
  return render_template('home.html', projects=projects.setup(), popular=popular)

@app.route('/flask/')
def flask():
    #Flask import uses Jinga to render HTML
    return render_template("fseries.html", projects=projects.setup())


@app.route('/hello/')
def hello():
    #Flask import uses Jinga to render HTML
    return render_template("hseries.html", projects=projects.setup())


@app.route('/popular-items/')
def popularitems():
  a = open("products.txt", "r").read()
  popular = a.split("\n")
  return render_template("popularitem.html", projects=projects.setup(), popular=popular)

@app.route('/calculator/', methods=['GET', 'POST'])
def calculator():
  if(request.method == 'POST'):
    form = request.form
    a = form['type']
    b = form['num1']
    c = form['num2']
    if a == 1:
      addition = np.add(b,c)
      result = "\nAdded values: \n" + addition
    elif a == 2:
      subtraction = np.subtract(b,c)
      result = "\nSubtracted values: \n" + subtraction
    elif a == 3:
      multiply = np.multiply(b,c)
      result = "\nMultiplied values" + multiply
    elif a == 4:
      divide = np.divide(b,c)
      result = "\nDivided values" + divide
    elif a == 5:
      power = np.power(b,c)
      result = "\nPower values" + power
    elif a == 6:
      modulus = np.mod(b,c)
      result = "\nModulus values" + modulus

    return render_template('calculator.html', result = result)
  return render_template('calculator.html')


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

# @app.route('/PSCI100/mock_trial')
# def mock_trial():
#     return render_template('mock_trial.html')

# @app.route('/PSCI100/supreme_court_decision_maker')
# def supreme_court_decision_maker():
#     return render_template('supreme_court_decision_maker.html')

if __name__ == '__main__':
    app.run(debug=True)
