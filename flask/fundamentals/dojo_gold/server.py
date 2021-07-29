#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
from typing import Counter
from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'thisSecretKey_isJustforDemonstration'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        # session['activity_list'] = []
        session['activity'] = ""
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'Farm':
        gold = random.randint(10,21)
        session['gold'] += gold
        # session['activity_list'].append(f"Earned {gold} golds from the farm!")
        session['activity'] += (f"\nEarned {gold} golds from the Farm!")
    if request.form['building'] == 'Cave':
        gold = random.randint(5,11)
        session['gold'] += gold
        # session['activity_list'].append(f"Earned {gold} golds from the Cave!")
        session['activity'] += (f"\nEarned {gold} golds from the Cave!")
    if request.form['building'] == 'House':
        gold = random.randint(2,6)
        session['gold'] += gold
        # session['activity_list'].append(f"Earned {gold} golds from the House!")
        session['activity'] += (f"\nEarned {gold} golds from the House!")
    if request.form['building'] == 'Casino':
        gold = random.randint(-50,50)
        session['gold'] += gold
        if gold > 0:
            # session['activity_list'].append(f"Earned {gold} golds from the Casino!")
            session['activity'] += (f"\nEarned {gold} golds from the Casino!")
        else:
            # session['activity_list'].append(f"Entered a casino and lost {gold} golds... Ouch.")
            session['activity'] += (f"\nEntered a casino and lost {gold} golds... Ouch.")
    return redirect('/')

@app.route('/restart')
def restart():
    session.clear()
    return redirect('/')

#this must be below ALL ROUTES
if __name__ =='__main__':
    app.run(debug=True)