from django.shortcuts import render
from django.http import HttpResponse
from .utils import registerUser, loginUser

import psycopg2

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

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to meme application.</h1>')



def register(request):
      
        
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
            response = registerUser(userData)
            
            # Print User Data
            print("Response: ")
            print(response)
            
            print('Users: ')
            print(response['total_users'])
            
            if response['statusCode'] == 200:
                return render(request, 'register.html',{'message' : 'Successfully recieved'})
            else:
                return render(request, 'register.html',{'message' : 'Already Registered'})
        else:
            return render(request,'register.html')
        
        
def login(request):
    
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
        
        response = loginUser(userData)
        
        if response['statusCode'] == 200:
            return render(request, 'login.html',{'message' : 'Successfully Logged In'})
        elif response['statusCode'] == 503 and response['message'] == 'passworderror':
            return render(request, 'login.html',{'message' : 'Password Not Matched'})
        else:
            return render(request, 'login.html',{'message' : 'Not Registered'})
        
        
        
    else:
        return render(request,'login.html')
        