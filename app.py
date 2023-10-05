from flask import Flask, render_template

app = Flask(__name__)

data = (
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    ("CRN1098asaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Databaseaaaaaaaaaaaaa", "15:00-16:00aaaaaaaaaaa", "Joe tekliaaaaaaaaaaaa", "40", "24" , "16", "zakhem 407a"),
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    ("CRN", "Database", "15:00", "Joe tekli", "40", "24" , "16", "zakhem 407"),
    
)
headers = (
    "CRN", "Name", "Schedule", "Instructor",
    "Capacity", "Active", "Remaining", "Location",
    "Register" 
)

@app.route("/registration")
def registration():
    return render_template("registration.html", courses = data, headers= headers)

@app.route("/home")
def home():
    return render_template("home.html", name="hah")
    
@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
