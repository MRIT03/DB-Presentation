# DB-Presentation
This project was developed to serve as a live demo of the usage of Flask in creating web apps as part of my Database and Systems course.

# Running the APP

Make sure to have flask installed in your directory by using the pip, like so: pip install flask
pip might be configured in a different way on your device so the command might be different, maake sure to configure it properly and install Flask.
After the proper library files are avaible, run the server using the command "python app.py", server will start running on your local host.

# Making changes to the frontend

In order to make changes to the frontend using tailwindcss, you need to run a script using the command "npm run create-css" which will be running in your terminal
this script rebuilds the tailwindcss files according to any changes you make to them.

# Structure of the code
- Static and templates folder contain all the files related to the frontend, including the html templates, the tailwindcss library, photos, images and fonts.
- App.py is the main application as it handles all the routings of the code. db_ops.py is a file that contain helper methods that were used in app.py
- database.py is a code meant to be run once to create the database, in case it has been deleted.

  
