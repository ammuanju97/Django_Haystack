from django.db import models

from django.conf import settings
class Book(models.Model):
        title = models.CharField(max_length=100, unique=True)
        slug = models.SlugField(unique=True)
        created_on = models.DateTimeField(auto_now_add=True)
        description = models.TextField()
        authors = models.ManyToManyField(settings.AUTH_USER_MODEL)
        
        def __unicode__(self):
            return self.title
        
        def __str__(self):
            return self.title