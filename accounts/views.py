from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    context = None
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/blog/')
        else:
            context = 'login credentials incorrect'
    if request.user.is_authenticated:
        return redirect('/blog/')
    else:
        return render(request, 'accounts/login.html', {'message':context})

def register(request):
    context = None
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password1']:
            if User.objects.filter(username=request.POST['username']).exists() == False:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                user.save()
                return redirect('/accounts/login/')
            else:
                context = 'username already exists'
        else:
           context = 'both passwords should match'
    return render(request, 'accounts/register.html',{'message':context})

def logout(request):
    auth.logout(request)
    return redirect('/accounts/login/')