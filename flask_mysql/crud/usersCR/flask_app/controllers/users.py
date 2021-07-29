from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import user


@app.route('/users')
def read():
    return render_template("readAll.html", all_users = user.get_all())

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

@app.route('/users/<int:id>')
def show(id):
    return render_template("readOne.html", user_one = user.get_one(id))

@app.route('/users/<int:id>/edit')
def edit(id):
    return render_template("edit.html", user_one = user.get_one(id))

@app.route('/users/<int:id>/edit_user', methods=['POST'])
def edit_user(id):
    data = {
        "id": id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    user.update(data)
    return redirect('/users')

@app.route('/delete/<int:id>')
def delete(id):
    user.delete_one(id)
    return redirect('/users') 

@app.route('/')
def new():
    return redirect('/users')   