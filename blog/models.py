from django.db import models
from html import unescape
from django.utils.html import strip_tags
from bs4 import BeautifulSoup
# Create your models here.
# blog/models.py

class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
	    verbose_name_plural = "categories"
	
    def __str__(self):
    	return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)	
    def __str__(self):
    	return self.name

FEATURED_CHOICES =[
	('yes', 'featured'),
	('no', 'not_featured')
]

WORDS_PER_MINUTE = 100

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    body_img = models.CharField(max_length=255, blank=True)
    body_two = models.TextField(blank=True)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    tag = models.ManyToManyField("Tag", related_name="posts")
    featured = models.CharField(max_length=3, choices =FEATURED_CHOICES)
    cover_image = models.CharField(max_length=255)
    
    def get_read_time(self):
        soup = BeautifulSoup(self.body, 'html.parser')
        text = soup.get_text()
        word_count = len(text.split())
        read_time = round(word_count / WORDS_PER_MINUTE)
        return read_time
        
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.author} on '{self.post}'"
