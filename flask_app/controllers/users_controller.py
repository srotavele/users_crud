from flask import Flask, render_template, request, redirect, session
from ..models.users_model import User
from flask_app import app


@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", my_users = users)


@app.route('/user/form')
def new_user_form():
    return render_template('Create.html')


@app.route('/user/new', methods = ['POST'])
def creates_user():
    user_id = User.create(request.form)
    return redirect(f"/show_user/{user_id}")


@app.route('/show_user/<int:user_id>')
def show_one_user(user_id):
    this_user = User.get_one({'id': user_id })
    print(this_user)
    return render_template("read_one.html", user = this_user)


@app.route('/show_edit_user/<int:user_id>')
def show_edit_user(user_id):
    user = User.get_one({'id': user_id })
    return render_template('edit_user.html', user = user)


@app.route('/edit_user/', methods = ['POST'])
def edit_one_user():
    user_id = User.edit_one(request.form)
    return redirect('/')


@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    User.delete_one({'id': user_id})
    return redirect('/')

