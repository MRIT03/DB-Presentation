import sqlite3


#This page defines a few functions to be used 
def authenticate(username, password):
    
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    cur.execute('SELECT password from Students WHERE email = ?', (username, ))
    correct_pass = cur.fetchall()[0][0]
    cur.close()
    return password == correct_pass

def retrieve_courses():
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    cur.execute('SELECT * from Courses')
    fetched = cur.fetchall()
    cur.close()
    return fetched

def add_registration(studentID, courseID):
    message = "You already registered this course!"
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    count = check(studentID, courseID) #checks if the student is already registered
    if count == 0:
        cur.execute('INSERT INTO Registers (studentID, CourseID, semester) VALUES (?,?,?)', (studentID, courseID, "Fall2023"))
        connection.commit()
        reduce_remaining(courseID) #reduce remaining seats 
        message = "You have successfully registered course " + courseID
    cur.close()
    return message

def remove_registration(studentID, courseID):
    message = "You have successfully dropped out of course " + courseID
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    cur.execute('DELETE FROM Registers WHERE studentId = ? AND courseID = ? AND semester = ?', (studentID, courseID, "Fall2023"))
    connection.commit()
    increase_remaining(courseID) #increase remaining seats
    cur.close()
    return message

  
    
def check(studentID, courseID):
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    cur.execute('SELECT COUNT (*) FROM registers WHERE (studentID, courseID) = (?,?)', (studentID, courseID))
    count = cur.fetchone()[0]
    cur.close()
    return count
    
#finds the courses of the specific student   
def retrieve_my_Courses(studentID):
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    cur.execute('SELECT courseID from Registers WHERE studentID = ?',(studentID,))
    courseID = cur.fetchall()
    list = []
    for id in courseID:
        list.append((retrieve_course(id[0])))
    cur.close()
    return list

#finds name,CRN,schedule, instructor of a course provided the id
def retrieve_course(courseID):
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    cur.execute('SELECT name,courseID,schedule,instructorName from Courses WHERE courseID = ?',(courseID,))
    course = cur.fetchone()
    cur.close()
    return course

def retrieve_studentID(student_identifier):
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    cur.execute('SELECT studentId from Students WHERE email = ?', (student_identifier, ))
    id = cur.fetchall()[0][0]
    cur.close()
    return id

def retrieve_courseId(course_identifier):
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    cur.execute('SELECT courseID from Courses WHERE name = ?', (course_identifier, ))
    id = cur.fetchall()[0][0]
    cur.close()
    return id

def clear_courses():
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    cur.execute('DELETE FROM Registers')
    connection.commit()
    cur.close()
    
def reduce_remaining(courseID):
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    cur.execute('Select active,rem FROM Courses WHERE courseID = ?', (courseID,))
    list =cur.fetchone()
    act = list[0]
    act +=1
    rem = list[1]
    rem -=1
    cur.execute('UPDATE Courses SET active = ?, rem = ? WHERE courseID = ?', (act, rem, courseID) )
    connection.commit()
    cur.close() 

def increase_remaining(courseID):
    connection = sqlite3.connect('my-database.db')
    cur = connection.cursor()
    cur.execute('SELECT active,rem FROM Courses WHERE courseID = ?', (courseID,))
    list =cur.fetchone()
    act = list[0]
    act -=1
    rem = list[1]
    rem +=1
    cur.execute('UPDATE Courses SET active = ?, rem = ? WHERE courseID = ?', (act, rem, courseID) )
    connection.commit()
    cur.close() 
