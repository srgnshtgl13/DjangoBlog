from django.urls import path, re_path, include
from userprofile.views import *

app_name = 'userprofile'

urlpatterns = [
    re_path(r'^myprofile/', ProfileView.as_view(), name='profile'),
    
]