from django.db import models

# Create your models here.
class BlogCreate(models.Model):
    blogid = models.AutoField(primary_key=True)
    blogtitle = models.CharField(max_length = 30)
    blogdescription = models.CharField(max_length = 2000)
    blogimage = models.ImageField(upload_to='media/')
