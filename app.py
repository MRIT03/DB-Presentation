from flask import Flask, render_template, redirect, request, url_for, flash, session
from datetime import timedelta
from db_ops import *
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


headers = (
    "CRN", "Name", "Schedule", "Instructor",
    "Capacity", "Active", "Remaining", "Location",
    "Register" 
)

@app.route("/")
def start():
    return redirect("/login")

@app.route("/registration")
def registration():
    if "user" not in session:
        return redirect(url_for("login"))
    data = retrieve_courses()
    message = session["message"]
    return render_template("registration.html", courses = data, headers= headers, message = message)

@app.route("/myCourses")
def myCourses():
    if "user" not in session:
        return redirect(url_for("login"))
    headers2 = (headers[1], headers[0], headers[2], headers[3], headers[8])
    std_id = retrieve_studentID(session["email"])
    my_courses = retrieve_my_Courses(std_id)
    message = session["message"]
    return render_template("myCourses.html", courses = my_courses, headers = headers2, message = message)
    

@app.route("/home")
def home():
    session['message'] = None
    if "user" in session:
        user = session["user"]
        return render_template("home.html", name=user)
    return redirect(url_for("login"))
    
@app.route("/login", methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == "POST" and 'email' in request.form and 'password' in request.form:
        email= request.form['email']
        password = request.form['password']
        try:
            authentication = authenticate(username=email, password=password)
        except Exception as e:
            authentication = False

        if authentication:
            name = email[0:email.index(".")] #grabs the first name of the user
            session["user"] = name
            session["email"] = email
            return redirect("/home")
        else:
            msg = "Incorrect username or password"

    return render_template("login.html", msg = msg)

@app.route("/add_course", methods=['POST'])
def add_course():
    course_id = request.form['course_id']
    print(course_id)
    std_id = retrieve_studentID(session["email"])
    std_id = retrieve_studentID(session["email"])
    session["message"] = add_registration(std_id, course_id)
    return redirect(url_for('registration'))

@app.route("/remove_course", methods=['POST'])
def remove_course():
    course_id = request.form['course_id']
    std_id = retrieve_studentID(session["email"])
    session["message"] = remove_registration(std_id, course_id)
    return myCourses()

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
