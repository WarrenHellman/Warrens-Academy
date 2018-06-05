# you just gotta import these modules
from flask import Flask, render_template, request, redirect
#need to define the app name
app = Flask(__name__)
#our index route handles the redering of the form in root
@app.route('/')
def index():
    return render_template('index.html')
#This route handles form submission
#we have to define which HTTP method is allowed for this route
@app.route('/users', methods=['POST'])
def create_user():
    print 'Got Post Info'
    name = request.form['name']
    email = request.form['email']
    #redirects back to the '/' root route
    return redirect('/')

app.run(debug=True)