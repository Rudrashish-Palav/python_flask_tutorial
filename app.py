from flask import Flask, render_template
"""
We create an instance of Flask class,
which will be our WSGI (Web Server Gateway Interface) application
"""

### WSGI Application 
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')


if __name__ == "__main__" :
    app.run(debug=True)