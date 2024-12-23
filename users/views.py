from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm , ProfileUpdateForm , UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"{username} your account has been successfully created! Login Now")
            return redirect('blog-login-page')
    else:
        form=UserRegisterForm()
    return render(request,"Html/register.html",{'form':form})

@login_required(login_url='blog-login-page')   
def profile(request):
    
    return render(request,"Html/profile.html")

@login_required(login_url='blog-login-page') 
def profileUpdate(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Profile Has Been Updated!!')
            return redirect('blog-profile-page')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    
    context={
        "u_form":u_form,
        "p_form":p_form
    }
    return render(request,"Html/profile_update.html",context)