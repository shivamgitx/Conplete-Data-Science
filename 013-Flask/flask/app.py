from flask import Flask

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''

### WSGI application
app=Flask(__name__)

@app.route("/")                      # decorator , helps to bind a function to a url
def welcome():
    return "Welcome to flask"

@app.route("/index")                      
def index():
    return "Welcome to index page"


if __name__ == '__main__':          # this is the entry point of any.py file
    app.run(host="127.0.0.1", port=8000, debug=True)      # debug=true hepls to run the app in debug mode i.e. while developing the changes will be reflected immediately