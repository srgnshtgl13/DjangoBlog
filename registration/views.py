from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import View
from registration.forms import UserCreateForm
from django.contrib.auth import authenticate, login, logout
from userprofile.models import Profile
from django.utils import timezone


class MySignUpView(View):
    form_class = UserCreateForm
    template_name = 'registration/sign_up.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            """
            u = User.objects.create_user(
                form.cleaned_data.get('username'),
                request.POST['email'],  # request.POST['email'],
                form.cleaned_data.get('password1'),
                is_active=True
            )"""
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.email = request.POST['email']
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = True
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            new_user = authenticate(username=form.cleaned_data.get(
                'username'), password=form.cleaned_data.get('password1'))
            login(request, new_user)
            
            # Fix Visiting UserProfile Page Error: if we don't create a profile object and save the field as null 
            # we will get an error when we visit the user profile file
            profile = Profile()
            profile.user = new_user
            profile.department = ""
            profile.bio = ""
            profile.location = ""
            profile.save()
            # TODO Display message and redirect to login
            # return HttpResponseRedirect('/accounts/login/?next=/')
            # TODO Display message and redirect to home page
            return redirect('home')
        return render(request, self.template_name, {'form': form})


class MyLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("home")
