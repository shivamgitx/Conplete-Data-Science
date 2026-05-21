from flask import Flask,render_template      #render_template is used to render/redirect the html file

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''

### WSGI application
app=Flask(__name__)

@app.route("/")                      # decorator , helps to bind a function to a url
def welcome():
    
    return "<html><H1>Welcome to flask</H1></html"

@app.route("/index")                      
def index():
    return render_template("index.html")


if __name__ == '__main__':          # this is the entry point of any.py file
    app.run(debug=True)      # debug=true hepls to run the app in debug mode i.e. while developing the changes will be reflected immediately