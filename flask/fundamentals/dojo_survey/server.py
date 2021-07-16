#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'thisSecretKey_isJustforDemonstration'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session ['name'] = request.form['name']
    session ['location'] = request.form['location']
    session ['language'] = request.form['language']
    session ['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    if 'name' not in session:
        return redirect ('/')
    return render_template('result.html')

if __name__ =='__main__':
    app.run(debug=True)