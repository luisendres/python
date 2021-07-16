from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import user


@app.route('/users')
def read():
    users = user.get_all()
    print(users)
    return render_template("readAll.html", all_users = users)

@app.route('/users/create')
def create():
    return render_template("create.html")

@app.route('/users/create_user', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    user.save(data)
    return redirect('/users')   

@app.route('/')
def new():
    return redirect('/users')   