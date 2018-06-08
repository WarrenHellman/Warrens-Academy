from flask import Flask, render_template, redirect, request, flash, session
# I spend a lot of time on this. Formatting can still be updated to smooth out the inputs and 
app= Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/results', methods=['POST'])
def showResults():
    result = {}

    result['name']=request.form['name']
    if len(request.form['name']) < 1:
        flash("Name field cannot be empty")
        return redirect('/')
    result['city']=request.form['city']
    result['language']=request.form['language']
    result['comment']=request.form['comment']
    if len(request.form['comment'])<1:
        flash("Comment field is NOT optional")
        return redirect('/')
    if len(request.form['comment'])>120:
        flash("Max comment length is 120 characters. Don't be so opinionated!")
        return redirect('/')
    return render_template('results.html', result=result)

app.run(debug=True)