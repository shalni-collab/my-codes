from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from universe.models import galaxy,ma
from universe.models import rats
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.shortcuts import render
from universe.models import galx


# Create your views here.



def index(request):
      if request.user.is_anonymous:
            return render(request, 'base.html')
      else:
           return redirect('home')
     
    
     
      allpost=galaxy.objects.all()
      context={'allpost':allpost}
      return render(request,'base.html',context)
 
     
   

     
   
         

def inde(request):
       if request.user.is_anonymous:
            return redirect('signin')
    
    
     
   
     
    
       allpost=galaxy.objects.all()
       context={'allpost':allpost}
     
       return render(request, 'index.html',context)
     

# Create your views here.
def img(request):
     allpost=ma.objects.all()
     context={'allpost':allpost}
     
       
     return render(request, 'img.html',context)
def vid(request):
      allpost=galx.objects.all()
      context={'allpost':allpost}
     
    
      return render(request, 'vid.html',context)
def car(request):
     allpost=rats.objects.all()
     context={'allpost':allpost}
     
     
     

     
     return render(request, 'car.html',context)
def signin(request):
      if request.method =="POST":
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
              login(request, user)
            
            return redirect('home')
            
        # A backend authenticated the credentials
      else:
                 
           return render(request, 'signin.html')
     
     
      return render(request,'signin.html')
def signup(request):
    if request.method =="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST.get('lname',False)
        email=request.POST['email']
        birthday=request.POST.get('birthday',False)
        phone=request.POST['phone']
        password=request.POST['password']
        chek_user=User.objects.filter(username=username).first()
        if chek_user:
            return redirect('/invalid')
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        
        return redirect('/signin')
    return render(request,'signup.html')
def invalid(request):
     return render(request,'invalid.html')
def signout(request):
     logout(request)
     return redirect('home')
     return render(request, 'logout.html')
     

   
          
     
         
     
