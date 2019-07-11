from django.shortcuts import render, get_object_or_404, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from post.models import Post, Category, Comment
from django.contrib.auth.models import User
from django.views.generic.list import MultipleObjectMixin
from .forms import CommentForm
from django.http import HttpResponseForbidden
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(ListView):
    model = Post
    context_object_name = 'all_posts'
    template_name = 'post/index.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        all_posts = Post.objects.all()
        if query:
            all_posts = all_posts.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(category__name__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(user__username__icontains=query)
            ).distinct()
        elif query == '':
            all_posts = ''
        return all_posts


class PostCategory(DetailView):
    model = Category
    template_name = 'post/post-category.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(PostCategory, self).get_context_data(**kwargs)
        # get post list by category
        # object_list = Post.objects.filter(category=self.object)
        object_list = self.object.post_category.filter()
        query = self.request.GET.get('q')
        if query:
            object_list = object_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(category__name__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(user__username__icontains=query) 
            ).distinct()
        # define the paginator and give to paginator the post_list=objectlist
        paginator = Paginator(object_list, self.paginate_by)
        # get page
        page = self.request.GET.get("page")
        # send the variable to template
        context['categories'] = Category.objects.all()
        context['category_posts'] = paginator.get_page(page)
        return context


class PostUser(ListView):
    model = Post
    template_name = 'post/post-user.html'
    paginate_by = 2

    def get_queryset(self):
        qs = Post.objects.all()
        return qs.filter(user__username__icontains=self.kwargs['username'])


class PostDetail(DetailView):
    model = Post
    template_name = 'post/post-detail.html'
    

    # list means get posts which they are the same category with this object
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        form = CommentForm(self.request.POST or None)
        cat = self.get_object().category
        if cat:
            context['list'] = cat.post_category.all()[:10]
        context['categories'] = Category.objects.all()
        context['form'] = form
        return context

    #@method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """ # you can use method_decorator or you can use the method like below
        if not request.user.is_authenticated:
            return HttpResponseForbidden()"""
        if not request.user.is_authenticated:
            form = CommentForm(request.POST or None)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post=self.get_object()
                comment.name = request.POST['name']
                comment.save()
                messages.success(request, 'You have made it!.', extra_tags='alert alert-success')
                return HttpResponseRedirect(self.get_object().get_absolute_url()+"#success-comment")
            else:
                messages.error(request,"Form error",extra_tags='alert alert-danger')
                return HttpResponseRedirect(self.get_object().get_absolute_url()+"#form-error")

        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.created_by = request.user
            

            comment.save()
            messages.success(request, 'You have made it!.', extra_tags='alert alert-success')
            return HttpResponseRedirect(self.get_object().get_absolute_url()+"#success-comment")
        else:
            messages.error(request,"Form error",extra_tags='alert alert-danger')
            return HttpResponseRedirect(self.get_object().get_absolute_url()+"#form-error")


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    template_name="post/post-create.html"
    model=Post
    fields = ["title","category","image","content"]


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.object.get_absolute_url())
    


    
    
