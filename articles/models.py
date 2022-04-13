from django.db import models
from django.db.models.signals import pre_save, post_save 
from django.urls import reverse
from django.utils import timezone


from .utils import slugify_instance_title

# Create your models here.
class Article(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, 
    auto_now=False, default=timezone.now, null=True, blank=True)

    def save(self, *args, **kwargs):
        #if self.slug is None:
           # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        
        return reverse("article-detail", kwargs={"slug": self.slug})
        #return f'/articles/{self.slug}/'


def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created,*args, **kwargs):
    print('ppost_save')
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)

