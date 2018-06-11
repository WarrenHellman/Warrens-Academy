from flask import Flask, render_template, redirect, request, session

app=Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random
import datetime

@app.route('/')
def index():
    session['gold']=0
    session['activity']=[]
    return render_template('index.html', gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['building']=='farm':
        val = random.randrange(10,21)
        session['gold']=random.randrange(10,21)
        activity= "-Earned "+str(val)+" gold from the farm! "+str(datetime.datetime.now())
        session['activity'].append(activity)
    elif request.form['building']=='cave':
        val = random.randrange(5,11)
        session['gold']+=val
        activity= "-Earned "+str(val)+" gold from the cave! "+str(datetime.datetime.now())
        session['activity'].append(activity)
    elif request.form['building']=='house':
        val = random.randrange(2,6)
        session['gold']+=val
        activity= "-Earned "+str(val)+" gold from the house! "+str(datetime.datetime.now())
        session['activity'].append(activity)
    else:
        val = random.randrange(-50,51)
        session['gold']+=val
        if val>0:
            activity= "-Went into the casino and won "+str(val)+" gold! Yes! "+str(datetime.datetime.now())
            session['activity'].append(activity)
        elif val<0:
            val*=-1
            activity= "-Went into the casino and lost "+str(val)+" gold! Yikes! "+str(datetime.datetime.now())
            session['activity'].append(activity)
        else:
            activity= "-Went into the casino and left with what you came with. Could have been worse! "+str(datetime.datetime.now())
            session['activity'].append(activity)
    return render_template('index.html', gold=session['gold'], activity=session['activity'])

app.run(debug=True)