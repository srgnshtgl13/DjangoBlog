from django.shortcuts import render, redirect, get_object_or_404, Http404, HttpResponseRedirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from userprofile.forms import ProfileForm,PersonalInfoForm
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, UpdateView):
    
    
    template_name = 'profile/form.html'
    login_url = '/accounts/login/'
    
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        personelform = PersonalInfoForm(request.POST or None, instance=user)
        profileform = ProfileForm(request.POST or None, instance = user.user_profile)
        context ={
            'profileform': profileform,
            'personalform':personelform,
            'email': user.email,
            'username': user.username,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        personelform = PersonalInfoForm(request.POST or None, instance=user)
        profileform = ProfileForm(request.POST or None,instance = user.user_profile)
        if profileform.is_valid():
            profileform.save()
            messages.success(request, 'Profile Info Updated', extra_tags='alert alert-success')
            return HttpResponseRedirect("profile/myprofile?profile=ok")
        elif personelform.is_valid():
            personelform.save()
            messages.success(request, 'Personal Info Updated', extra_tags='alert alert-success')
            return HttpResponseRedirect("profile/myprofile?personal=ok")
        else:
            messages.error(request,"Form error",extra_tags='alert alert-danger')
            return HttpResponseRedirect("profile/myprofile")




