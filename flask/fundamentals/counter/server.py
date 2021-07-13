#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'thisSecretKey_isJustforDemonstration'

@app.route('/')
def counter():
    if 'i' not in session:
        session['i'] = 0
    session['i'] +=1
    return render_template('index.html', i = session['i'])

@app.route('/restart')
def restart():
    session.clear()
    # session['i'] = 0
    return redirect('/')

@app.route('/plus')
def plus():
    session['i'] += 1
    return redirect('/')
#this must be below ALL ROUTES
if __name__ =='__main__':
    app.run(debug=True)