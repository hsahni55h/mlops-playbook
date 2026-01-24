# Jinja2 template engine (building URL dynamically)

from flask import Flask, render_template, request, redirect, url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "</html><H1>basic flask app<H1></html>"


@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


# variable rule 
# restricting a parameter with a datatype that we are passing
@app.route('/result/<int:score>')
def success(score):
    res=""
    if score > 50:
        res ="PASS"
    else:
        res = "FAIL"
    return render_template('result0.html', results = res)


@app.route('/successresults/<int:score>')
def successresults(score):
    res=""
    if score > 50:
        res ="PASS"
    else:
        res = "FAIL"

    exp = {'score': score, "res": res}

    return render_template('result2.html', results = exp)


# if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result1.html', results = score)

# if condition
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result1.html', results = score)


@app.route('/submit', methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science)/4
    
    else:
        return render_template('getresult.html')
    return redirect(url_for('successresults', score = total_score))


if __name__=="__main__":
    app.run(debug=True)