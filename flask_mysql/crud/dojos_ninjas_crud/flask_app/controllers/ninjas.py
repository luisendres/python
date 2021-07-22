from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def create():
    return render_template("ninja.html", all_dojos =  Dojo.get_all_dojos())

@app.route('/ninjas/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        "dojo_id": request.form['dojo_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age']
    }
    Ninja.save_ninja(data)
    redirect_here = "/dojos/" + request.form['dojo_id']
    return redirect(redirect_here)
    
