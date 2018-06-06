from flask import Flask, render_template, redirect, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def colorChange():
    result= {}
    result['red']=request.form['red']
    result['blue']=request.form['blue']
    result['green']=request.form['green']
    red = result['red']
    blue = result['blue']
    green = result['green']
    return render_template('index.html', red=red, blue=blue, green=green, result=result)

app.run(debug=True)