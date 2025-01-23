from django.db import models
# Create your models here.


# defining calsses for the post of blogs

class Post(models.Model):
    # model for Post db
    #image = models.ImageField(null=True , blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)
    #author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    

# category class for blog posts
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
