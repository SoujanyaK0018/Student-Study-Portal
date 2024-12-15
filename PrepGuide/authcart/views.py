from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        name=request.POST['name']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'signup.html')                   
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Email is Taken")
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password,first_name=name)
        
        user.is_active=True
        user.save()
        return redirect('/auth/login/') 
    return render(request,"signup.html")
def handlelogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['pass1']
        myuser=authenticate(username=email,password=password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successfull")
            return redirect('/')
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect('/auth/login');
    return render(request,'login.html');
def handlelogout(request):
    logout(request)
    return redirect('/')









