from django.urls import path, re_path, include
from post.views import *

app_name = 'post'
urlpatterns = [
    
    re_path(r'^$', PostList.as_view(), name='index'),

    re_path(r'^create/', PostCreateView.as_view(), name="create"),

    re_path(r'^(?P<slug>[\w-]+)/(?:instance=(?P<created>[\w-]+)/)?$', PostCategory.as_view(), name='category-post'),
    
    re_path(r'^(?P<username>[\w]+)/(?:index=(?P<index>[\w-]+)/)?$', PostUser.as_view(), name='user-post'),

    re_path(r'^(?P<slug>[\w-]+)/(?:publish=(?P<publish>[\w-]+)/)?$', PostDetail.as_view(), name='post-detail'),
    
]