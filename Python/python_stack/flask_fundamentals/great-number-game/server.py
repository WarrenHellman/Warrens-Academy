from flask import Flask, render_template, redirect, session, request

app=Flask(__name__)
import random
app.secret_key = 'ThisIsSecret'
number= random.randrange(1,101)

@app.route('/')
def index():
    # print 'Loaded'
    number= random.randrange(1,101)
    session['guess']=number
    print session['guess']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    # print 'Redirected'
    print "Request form value "+str(request.form['guess-box'])
    print "Session number "+str(session['guess'])
    low=""
    high=""
    nailedIt=""
    if int(request.form['guess-box'])>session['guess']:
        print 'Too high!'
        high="Too high!"
    elif int(request.form['guess-box'])<session['guess']:
        print 'Too low!'
        low="Too Low!"
    else:
        print "Got it!"
        nailedIt="Got it!"
    return render_template('index.html', high=high, low=low, nailedIt=nailedIt)
@app.route('/restart', methods=['POST'])
def restart():
    session.pop('guess')
    # number= random.randrange(1,101)
    # session['guess']=number
    return redirect('/')
app.run(debug=True)