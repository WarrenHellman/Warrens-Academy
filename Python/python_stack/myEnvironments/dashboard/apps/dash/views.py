# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
# imports our defined classes
from .models import User, Message, Comment
from django.contrib import messages
# Our dependencies. Running the app through the terminal, bycrypt is available. VS Code does not show bcrypt, hence the error
import bcrypt

# Create your views here.

# renders our landing page 
def index(request):
    return render(request, 'dash/index.html')

# When the signin page is visited, users are logged out if logged in. The session data for user level and current user ID are reset
def signin(request):
    if request.session['login']=='Log Out':
        request.session['login']='Sign In'
        request.session['user_id']=None
        request.session['user_level']=None
    else:
        request.session['login']='Sign In'
        request.session['user_level']=None
    return render(request, 'dash/signin.html')

# Checks password during login. Sets session data for admin or normal users as well as id and log in status
def passcheck(request):
    errors = User.objects.logvalidator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/signin')
    else:
        user = User.objects.get(email=request.POST['email'])
        # changes the nav bar 'sign in' to 'log out'. Effectively logs a user in
        request.session['login']='Log Out'
        request.session['user_id']=user.id
        # User level check and session data addition
        if user.user_level == 9:
            request.session['user_level']='admin'
            return redirect('/dashboard')
        else: 
            request.session['user_level']='normal'
            return redirect('/dashboard')

# load registration page. Perhaps session data should be wiped here. A session data removal function would be helpful
def register(request):
    return render(request, 'dash/register.html')

# loads the dashboard and shows admin dashbaord or regular dashboard. Guards agains non admin visiting the page by checking user level
def dashboard(request):
    if request.session['user_level']=='admin':
        if request.session['user_id']==None:
            return redirect('/signin')
        else:
            context = {
                'users':User.objects.all()
            }
            return render(request, 'dash/dashAdmin.html', context)
    else:
        context = {
            'users':User.objects.all()
        }
        return render(request, 'dash/dashboard.html', context)

# Renders the admin user editing page. If not an admin, it won't load
def edit(request, id):
    if request.session['user_level']=='admin':
        context= {
            'user': User.objects.get(id=id)
        }    
        return render(request, 'dash/edit.html', context)
    else:
        return redirect('/signin')

# deletes a user from the admin dashboard and database
def remove(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/dashboard')

# Validates password and encrypts it
def updatepwd(request, id):
    user = User.objects.get(id=id)
    errors = User.objects.updateValidator(request.POST)
    if len(errors):
        id=user.id
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/edit/'+str(id))
    else:
        user = User.objects.get(id=id)
        user.password = request.POST['password']
        hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        user.password = hashed
        user.save()
        return redirect('/dashboard')

# Lets an admin update user info
def update(request, id):
    user = User.objects.get(id=id)
    user.email = request.POST['email']
    user.first = request.POST['first']
    user.last = request.POST['last']
    if request.POST['user_level']=='Admin':
        user.user_level=9
    else:
        user.user_level=1
    user.save()
    return redirect('/dashboard')

# load the add new user page for admins
def add(request):
    return render(request, 'dash/add.html')

# Adds a new user through the add page and encrypts their password
def addUser(request):
    # Could make this DRY by making the error section and create user section their own functions
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/register')
    else:
        user = User.objects.create()
        user.email = request.POST['email']
        user.first = request.POST['first']
        user.last = request.POST['last']
        user.password = request.POST['pwd']
        hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        user.password = hashed
        user.user_level = 1
        user.save()

        return redirect('/dashboard', {'user':User.objects.get(id=request.session['user_id'])})

# processes registration data. First user is automatically an admin
def newUser(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/register')
    else:
        user = User.objects.create()
        id = user.id
        user.email = request.POST['email']
        user.first = request.POST['first']
        user.last = request.POST['last']
        user.password = request.POST['pwd']
        hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        user.password = hashed
        if user.id == 1:
            user.user_level = 9
        else: 
            user.user_level = 1
        user.save()
        if request.session['login']=='Sign In':
            request.session['login']='Log Out'
        request.session['user_id']=user.id
        return redirect('/dashboard', {'user':User.objects.get(id=id)})

# Loads the profile editing page only if the user is logged in
def editUser(request, id):
    user = User.objects.get(id=id)
    if user.id == request.session['user_id']:
        context = {
            'user' : User.objects.get(id=id)    
        }

        return render(request, ('dash/userEdit.html'), context)
    else: 
        return redirect('/signin')

# Adds a description to profile page
def description(request, id):
    user=User.objects.get(id=id)
    user.description = request.POST['description']
    user.save()
    return redirect('/dashboard')

# Loads user wall with access to all of the messages, users and comments to dynamically display each user's comments and messages
def userpage(request, id):
    context = {
        'user' : User.objects.get(id=id) ,
        'users' : User.objects.all(),
        'messages' : Message.objects.all().order_by('-created_at'),   
        'comments' : Comment.objects.all()
    }
    return render(request, ('dash/userpage.html'), context)

# When posting a message, this associates the poster that is logged in with the message being posted
def postmsg(request, id):
    user = User.objects.get(id=id)
    id= user.id
    context = {
        'user' : User.objects.get(id=id)    
    }
    message = Message.objects.create(content=request.POST['leavemsg'], user = User.objects.get(id=id))
    message.poster_id = request.session['user_id']
    message.save()
    return redirect('/users/show/'+str(id), context)

# When posting a comment, this associates the poster that is logged in with the comment being posted
def postcomment(request, id):
    message = Message.objects.get(id=id)
    id= message.id
    context = {
        'message' : Message.objects.get(id=id),
        'comments' : Comment.objects.all()
    }
    comment = Comment.objects.create(content=request.POST['leave-comment'], message = Message.objects.get(id=id))
    comment.poster_id = request.session['user_id']
    user = message.user_id
    comment.save()
    return redirect('/users/show/'+str(user), context)