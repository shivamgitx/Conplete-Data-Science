### building rl dynamically
### Variables url
### jinja 2 template engine

### jinja 2 template engine
'''
{{  }} expressions to print output in html
{%...%} conditions for loops
{#...#} this is for comments

'''


from flask import Flask,render_template      
from flask import request

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''

### WSGI application
app=Flask(__name__)

@app.route("/")                      
def welcome():
    
    return "<html><H1>Welcome to flask</H1></html"

@app.route("/index",methods=['GET'])                      
def index():
    return render_template("index.html")

@app.route('/submit',methods=['GET','POST'])                      
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}"
    return render_template("form.html")

#variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>50:
        res="pass"
    else:
        res="fail"
   
    return render_template('result.html',results=res)


#variable rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>50:
        res="pass"
    else:
        res="fail"

    exp={'score':score,'res':res}    
   
    return render_template('result1.html',results=exp)




if __name__ == '__main__':          
    app.run(debug=True)      