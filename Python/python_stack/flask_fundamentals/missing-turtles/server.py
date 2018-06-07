from flask import Flask, render_template, redirect, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja/')
def ninjaSlash():
    return render_template('ninja.html', color="")
@app.route('/ninja/<color>')
def color(color=None):
    print color
    return render_template('ninja.html', color=color)

app.run(debug=True)