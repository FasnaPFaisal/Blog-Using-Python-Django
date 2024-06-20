from django.db import models

# Create your models here.
class AddPost(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='img/')
    created_at = models.DateTimeField(auto_now_add=True)
    