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


if __name__ == "__main__" :
    app.run(debug=True)