from flask import Flask, render_template, redirect

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    comment = request.form['comment']
    return render_template('results.html', name = name, comment = comment)
app.run(debug=True)