from flask import Flask, render_template, request, redirect
from user_model import User

app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("read(all).html", users = users)

@app.route("/user/new")
def new_user_form():
    return render_template("create.html")

# route to creating a new user
@app.route("/user/create", methods = ['POST'])
def create_user():
    id = User.create(request.form)
    return redirect(f"/user/{id}/show")

# (SHOW USER)show the single user route(*needs to know about a single user)

@app.route("/user/<int:id>/show")
def get_one(id):
    data = { 'id' : id }
    user1 = User.get_one(data)  #method to call a single user
    return render_template("show_user.html", user = user1)
# ------------------------------------------------------------

# Edit User

@app.route("/user/<int:id>/edit")
def edit_user_form(id):
    data = {"id" : id}
    user = User.get_one(data)
    return render_template("user_edit.html", user = user)

@app.route("/user/<int:id>/edited", methods = ['POST'])
def edit_user(id):
    data = { 'id' : id,
            'first_name': request.form["first_name"],
            'last_name':request.form["last_name"],
            'email':request.form["email"]
            }
    User.edit_user(data)
    return redirect("/")
#--------------------------------------------------------
# delete user

@app.route("/user/<int:id>/delete")
def delete_user(id):
    data = {'id':id}
    User.delete_user(data)
    return redirect("/")


# error handler for 404 errors 
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"
# ----------------------------

if __name__ == "__main__":
    app.run(debug=True) 