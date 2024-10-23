from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')


@app.route('/successres/<int:score>')
def successres(score):
    res = ''
    if score >= 50 : 
        res = "PASS"
    else : 
        res = "FAIL"
    exp = {'score' : score, 'result' : res }

    return render_template('result1.html', result=exp) 


@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    total_score = 0 
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science+maths+c+data_science)/4
    else : 
        return render_template('get_result.html') 
    return redirect(url_for('successres', score = total_score)) 


if __name__ == "__main__" :
    app.run(debug=True)