from django.shortcuts import render
from basicapp import forms

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.



def index(request):
    return render(request,'base.html')

def register(request):
    user_obj=forms.UserForm()
    user_profile_obj=forms.UserProfileForm()
    registered=False
    if request.method=='POST':
        user_obj=forms.UserForm(data=request.POST)
        user_profile_obj=forms.UserProfileForm(data=request.POST)
        if (user_obj.is_valid() and user_profile_obj.is_valid()):
            user=user_obj.save()
            user.set_password(user.password)
            user.save()
            #print(user_obj)
            profile=user_profile_obj.save(commit=False)
            profile.user=user
            print(user_profile_obj)

           
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_obj.errors,user_profile_obj.errors)
    else:
        print('data was not posted')
    return render(request,'register.html',{'userform':user_obj,'user_pro':user_profile_obj,'registered':registered})

def login_user(request):
    if (request.method=="POST"):
        username1=request.POST.get('username')
        password1=request.POST.get('pass')
        print(username1,password1)

        user = authenticate(username=username1, password=password1)


        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('basicapp:index'))

            else:
                print('User is not active')
                return HttpResponse('user is not active!!')
        else:
            print("Incorrect user name and password")
            return render(request,'loginview.html',{'log_parm':True})
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('basicapp:index'))
        return render(request,'loginview.html',{'log_parm':False})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basicapp:index'))


