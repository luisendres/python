from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def read():
    return render_template("index.html", all_dojos =  Dojo.get_all_dojos())

@app.route('/dojos/create_dojo', methods= ['POST'])
def create_dojo():
    data = {
        "name": request.form['name']
    }
    Dojo.save_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<dojo_id>')
def get_ninjas(dojo_id):
    data = {
        'id': dojo_id
    }

    this_dojo = Dojo.get_ninjas_from_dojo(data)

    return render_template('dojos.html', this_dojo=this_dojo)

@app.route('/')
def new():
    return redirect('/dojos')  