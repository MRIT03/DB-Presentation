#This file is meant to be ran once as it creates the database required for the project with the 
#appropriate tables

import sqlite3

connection = sqlite3.connect('my-database.db')

cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Students (
            studentId integer PRIMARY KEY,
            name text,
            email text,
            year integer,
            password text
            );""")

cur.execute("""CREATE TABLE IF NOT EXISTS Courses (
            courseID integer PRIMARY KEY,
            name text,
            schedule text,
            instructorName text,
            cap integer,
            active integer,
            rem integer, 
            location text

            );""")


cur.execute("""CREATE TABLE IF NOT EXISTS Registers (
            studentId integer NOT NULL,
            courseID integer NOT NULL,
            semester text,
            FOREIGN KEY (studentId) REFERENCES Students (studentId),
            FOREIGN KEY (courseID) REFERENCES Courses (courseID)
            );""")

students = [
    (202300234, "Daisy Smith", "daisy.smith@lau.edu", 1, "DaisyMeRollin"),
    (202100123, "John Doe", "john.doe@lau.edu", 3, "DoeNot"),
    (202008973, "Elie Tannous", "elie.tannous@lau.edu",4, "ElieKopter"),
    (202100518, "Steven Mansour", "steven.mansour@lau.edu", 3, "Stivan")
]

courses = [
    (5000, "Database Systems", "MWF 12:00-12:50", "Joe Tekli", 40, 40, 0, "Zakhem 405"),
    (5001, "Control Systems", "MWF 1:00-1:50", "Noel Maalouf", 60, 56, 4, "Zakhem 406"),
    (5002, "Computer Architecture", "MFW 2:00-2:50", "Maria Abi Saad", 40, 15, 25, "Zakhem 508"),
    (5003, "Computer Programming", "TR 9:00-10:15", "Wissam Fawaz", 60, 60, 0, "Zakhem 406"),
    (5004, "Logic Design", "TR 12:00-1:15", "Zahi Nakad", 40, 39, 1, "Science 402")
]

cur.executemany("INSERT INTO Students (studentId, name, email, year, password) VALUES (?,?,?,?,?)", students)

cur.executemany("INSERT INTO Courses (courseID, name, schedule, instructorName, cap, active, rem, location) VALUES (?,?,?,?,?,?,?,?)", courses)

connection.commit()
connection.close()