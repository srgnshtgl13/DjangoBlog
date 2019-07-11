from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
import datetime
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=120)
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE, verbose_name = 'Author', related_name = 'post_user')
    category = TreeForeignKey('Category', null=True, on_delete = models.CASCADE, blank=True, related_name = 'post_category')
    image = models.ImageField(verbose_name="Image", null=True, blank=True,upload_to = 'post_image/')
    content = RichTextField(verbose_name="Content")
    publishing_date = models.DateTimeField(verbose_name='Publishing Date',auto_now_add=True)
    slug = models.SlugField(unique = True, editable = False, max_length=130)

    def __str__(self):
            return self.title
    
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug       # sluglari karsilastirmak icin unique_slug degiskeni olusturduk
        
        counter = 1
        while Post.objects.filter(slug = unique_slug).exists():  # veritabaninda atni isimde slug alani var mi diye kontrol sonra her while dongusun de counter 1 arttiriliyor islem essiz bir slug yaratilana kadar devam ediyor
            unique_slug = '{}-{}'.format(slug,counter)
            counter += 1
        return unique_slug
    
    def get_user_url(self):
        return reverse('post:user-post', kwargs={'username':slugify(self.user.username),'index':slugify(self.user.date_joined)})
    
    def get_absolute_url(self):
        return reverse('post:post-detail', kwargs={'slug': self.slug, 'publish':slugify(self.publishing_date)})
    
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs) # Call the real save() method
    
    class Meta:
        ordering = ['-publishing_date','id'] #postlarin tarihe gore enson eklenene gore siralanmasi ve tarihleri ayni olanlarin id ye gore siralanmasi.Eger publishing_date in onundeki tire olmasaydi postlar varsayilana gore eskiden yeniye gore siralanirdi.


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete = models.CASCADE, db_index=True)
    slug = models.SlugField(editable = False)
    created_date = models.DateTimeField(verbose_name='Created Date',auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('post:category-post', kwargs={'slug': self.slug, 'created':slugify(self.created_date)})
        # return "/post/{}".format(self.id)
    
    def save(self, *args, **kwargs):
       self.slug=slugify(self.name.replace('ı','i'))    
       return super(Category, self).save(*args, **kwargs) # Call the real save() method

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [ i.slug for i in ancestors]
            slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))
        return slugs

    def __str__(self):
            return self.name

class Comment(models.Model):
    created_by = models.ForeignKey('auth.User', on_delete = models.CASCADE, verbose_name = 'Author', null=True, blank=True, related_name = 'user_comments')
    name = models.CharField(max_length=120, null=True,blank=True)
    post = models.ForeignKey('Post', on_delete = models.CASCADE, verbose_name = 'Post', related_name='post_comments')
    content = models.TextField(verbose_name='Comment')
    created_date = models.DateTimeField(auto_now_add=True)