from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import profile_update
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    count = User.objects.count()
    return render(request, 'index.html', {'count': count})


def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # user= authenticate(username=username, password=password)
            # login(request, user)
            return redirect('home')
    else:  
        form = UserCreationForm
    return render(request, 'registration/signup.html', {'form':form})

@login_required
def profile(request):
    # update profile
    if request.method == 'POST':

        profile_form = profile_update(request.POST, instance=request.user.profile)
        if profile_form.is_valid:

            profile_form.save()
            messages.success(request, ('Your profile was updated successfully'))
            return redirect('profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:   
        form = profile_update
        return render(request, 'profile.html', {
            'form': form
        })
