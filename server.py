from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)
app.secret_key = "for safe keeping"



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






if __name__ == "__main__":
    app.run(debug=True)