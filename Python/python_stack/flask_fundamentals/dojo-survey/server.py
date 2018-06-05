from flask import Flask, render_template, redirect, request
# I spend a lot of time on this. Formatting can still be updated to smooth out the inputs and 
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/results', methods=['POST'])
def showResults():
    result = {}
    result['name']=request.form['name']
    result['city']=request.form['city']
    result['language']=request.form['language']
    result['comment']=request.form['comment']
    return render_template('results.html', result=result)

app.run(debug=True)