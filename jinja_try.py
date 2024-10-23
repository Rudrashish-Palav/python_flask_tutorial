### Jinja2 Template Engine
"""
{{ }} Expression to print output in html
{% %} conditions, for loops 
{# #} Comments 
"""

from flask import Flask, render_template, request
"""
We create an instance of Flask class,
which will be our WSGI (Web Server Gateway Interface) application
"""

### WSGI Application 
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/form", methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name'] ## the data from id "name"
        return f'Hello {name}!'
    return render_template('form.html')

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50 : 
        res = "PASS"
    else : 
        res = "FAIL"
    
    return render_template('result.html', result=res) 

## For Loop
@app.route('/successres/<int:score>')
def successres(score):
    res = ''
    if score >= 50 : 
        res = "PASS"
    else : 
        res = "FAIL"
    exp = {'score' : score, 'result' : res }

    return render_template('result1.html', result=exp) 

## If Loop
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('resultif.html', result=score) 




if __name__ == "__main__" :
    app.run(debug=True)