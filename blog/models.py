from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200,db_index=True, unique=True)

	class Meta:
		ordering = ('-title',)
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title

def get_absolute_url(self):
        return reverse('blog:category', args=[self.slug])

class Post(models.Model):
    category=models.ForeignKey(Category,related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    overview = models.TextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-title',)
	

def get_absolute_url(self):
	return reverse('blog:post-list')

def get_absolute_url(sself):
	return reverse('blog:article-detail',kwargs={
		'pk': self.pk
		})