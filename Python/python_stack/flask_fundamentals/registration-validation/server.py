from flask import Flask, session, flash, render_template, redirect, request

import re

app=Flask(__name__)
app.secret_key = "ThisIsSecret!"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r"[0-9]")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # empty field check, can you refactor this?
    first=str(request.form['first-name'])
    last=str(request.form['last-name'])
    if len(request.form['email'])<1:
        flash("Email cannot be empty")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif len(request.form['first-name'])<1:
        flash("First Name cannot be empty")
    elif not first.isalpha():
        flash("First name cannot include a number")
    elif not last.isalpha():
        flash("Last name cannot include a number")
    elif len(request.form['last-name'])<1:
        flash("Last Name cannot be empty")
    elif len(request.form['password'])<1:
        flash("Password cannot be empty")
    elif len(request.form['password'])<8:
        flash("Password must be a minimum of 8 characters")
    elif len(request.form['confirm-password'])<1:
        flash("Please confirm password")
    elif request.form['password']!=request.form['confirm-password']:
        flash('Passwords do not match')
    else:
        flash("Thank you, your information has been submitted")
    return redirect('/')

app.run(debug=True)
