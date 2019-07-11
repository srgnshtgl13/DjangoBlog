from django.contrib import admin
from .models import Post,Category
from mptt.admin import MPTTModelAdmin

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'publishing_date']
    list_display_links = ['publishing_date','user']
    search_fields = ['title','content']
    list_editable = ['title']
    list_filter = ['publishing_date']
    
    # save user to post_user related field automatically
    """
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    """
    # save user to post_user related field automatically
    
    
    # display post list by user
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        #if username = sergen display all post
        if request.user.username == "sergen":
            return qs
        #if username = sergen display all post
        return qs.filter(user=request.user)
    # display post list by user
    

    class Meta:
        model = Post
    

admin.site.register(Post , PostAdmin)
admin.site.register(Category , MPTTModelAdmin)
