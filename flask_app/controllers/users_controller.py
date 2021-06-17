from flask import Flask, render_template, request, redirect
from ..models.users import User
from flask_app import app


@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", my_users = users)

@app.route('/user/form')
def new_user_form():
    return render_template('/Create.html')

@app.route('/user/new', methods = ['POST'])
def creates_user():
    User.create(request.form)
    return redirect ('/')

@app.route('/show_user/<int:users_id>')
def show_one_user(users_id):
    user_get_one({'id': users_id})
    return render_template('/read_one.html')
