from flask import Flask, render_template, redirect, request, session
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=0
    return render_template('index.html')
@app.route('/button', methods=['POST'])
def button():

    session['count']+=1
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    # adds a reset button to the count
    session['count']=-1
    return redirect('/')

app.run(debug=True)