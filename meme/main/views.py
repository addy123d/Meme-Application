from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import registerUser, loginUser
from django.contrib.sessions.backends.db import SessionStore #For Session Storage 

import psycopg2

s = SessionStore()

# Connection to database

try:
    connection = psycopg2.connect(
            host = "127.0.0.1",
            port = "5432",
            database = "memestore",
            user="postgres",
            password="postgres"
    )
    
    print("Database Connected")
except Exception as e:
    print("Error: ",e)
    print("Database Connection Failed")
    
connection.autocommit = True # "autocommit" set to True, so you don't have to commit your queries.
cursor = connection.cursor()

# Middleware

def checkSession():
    try:
        email = s['email']
        return True
    except Exception as e:
        print("Error: ",e)
        return False

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to meme application.</h1>')



def register(request):
    
        sessionExists = checkSession()
        
        if sessionExists == False:
        
            if request.method == 'POST':
                
                # Collect all data from client
                name = request.POST['name']
                contact = request.POST['contact']
                email = request.POST['email']
                password = request.POST['password']
                
                # Print
                print(f'Name: {name}')
                print(f'Contact: {contact}')
                print(f'Email: {email}')
                print(f'Password: {password}')  
                
                # Create User Dictionary
                userData = {
                    'name' : name,
                    'contact' : contact,
                    'email' : email,
                    'password' : password
                }     
                
                # Register User   
                response = registerUser(userData,cursor)
                
                # Print User Data
                print("Response: ")
                print(response)
                
                if response['statusCode'] == 200:
                    # Session Store
                    s['email'] = userData['email']
                    s['password'] = userData['password']
                    
                    print('Session: ')
                    print(s)
                    
                    
                    # return render(request, 'register.html',{'message' : 'Successfully recieved'})
                    return redirect('/memes/')
                else:
                    return render(request, 'register.html',{'message' : 'Already Registered'})
            else:
                return render(request,'register.html')
            
        else:
            return redirect('/memes/')
        
        
def login(request):
    
    sessionExists = checkSession()
    
    if sessionExists == False:
    
        if request.method == 'POST': #We are checking the type of request, GET OR POST
            email = request.POST['email']
            password = request.POST['password']
            
            # Print
            print('Email: ')
            print(email)
            
            print('Password: ')
            print(password)
            
            # Create user dict.
            
            userData = {
                'email' : email,
                'password' : password
            }
            
            response = loginUser(userData,cursor)
            
            if response['statusCode'] == 200:
                # Session Store
                s['email'] = userData['email']
                s['password'] = userData['password']
                    
                print('Session: ')
                print(s)
                
                # return render(request, 'login.html',{'message' : 'Successfully Logged In'})
                return redirect('/memes/')
            elif response['statusCode'] == 503 and response['message'] == 'passworderror':
                return render(request, 'login.html',{'message' : 'Password Not Matched'})
            else:
                return render(request, 'login.html',{'message' : 'Not Registered'})
            
            
            
        else:
            return render(request,'login.html')
    
    else:
        return redirect('/memes/')
    
def logout(request):
    try:
        s.clear()
        return redirect("/login/")
    except:
        return redirect("/memes/")
    
def getmemes(request):
    sessionExists = checkSession()
    
    if sessionExists == False:
        return redirect("/login/")
    else:
        return HttpResponse('''<h1>This is a private page, only for authenticated user</h1>
                                <a href="/logout"><button>Logout</button></a>"''')
    
    

        