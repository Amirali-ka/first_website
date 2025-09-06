from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username=request.POST['username']
                password=request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
            form=AuthenticationForm()
    else:
        return redirect('/')
    return render(request,'accounts/login.html')
def logout_view(request):
    return render(request,'accounts/logout.html')
def signup_view(request):
    return render(request,'accounts/signup.html')