from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic.base import TemplateView
from post.models import Post,Category


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)

        query = self.request.GET.get('q')
        if query:
            all_posts = Post.objects.filter(
                Q(title__icontains=query)|
                Q(content__icontains = query) |
                Q(category__name__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(user__username__icontains=query)
            ).distinct()
            paginator = Paginator(all_posts,3)
            page = self.request.GET.get("page")
            context['posts']=paginator.get_page(page)
            context['categories'] = Category.objects.all()
            return context

        # context['posts'] = Post.objects.all()[:5]  # this make the same thing with order_by("-id")[:5]
        context['posts'] = Post.objects.order_by("-id")[:5] # i think we can use this 
        context['categories'] = Category.objects.all()
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'


"""
#it can be used the place of HomePageView class

def home_view(request):
    posts = Post.objects.order_by("-id")[:5]
    categories = Category.objects.all()

    query = request.GET.get('q')
    if query:
        posts_list = Post.objects.filter(
            Q(title__icontains=query)|
            Q(content__icontains = query) |
            Q(category__name__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__username__icontains=query)
        ).distinct()
        paginator = Paginator(posts_list,1)
        page = request.GET.get("page")
        posts=paginator.get_page(page)
        context = {
            'categories': categories,
            'posts':posts
        }
        return render(request,'home.html', context)

    context={
        'posts':posts,
        'categories':categories
    }
    return render(request,'home.html',context)
"""