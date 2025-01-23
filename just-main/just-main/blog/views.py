from django.shortcuts import render
from django.shortcuts import render,redirect
from blog.forms import ImageForm
from .models import Image
# Create your views here.
def blog(request):
    if request.method == "POST":
     form=ImageForm(data=request.POST,files=request.FILES)
     if form.is_valid():
      form.save()
      obj=form.instance
      
     return render(request,"blog.html",{"obj":obj})
    else:
         form=ImageForm()
    img=Image.objects.all()
    return render(request,"blog.html",{"img":img,"form":form})
    
   


 




    

# Create your views here.
