from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to meme application.</h1>')



def register(request):
                  
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            
            
            print(f'Email: {email}')
            print(f'Password: {password}')  
            
            # users = [{'email': email, 'password':password}, {}, {},....]          
            
            return render(request, 'register.html',{'message' : 'Successfully recieved'})
        else:
            return render(request,'register.html')