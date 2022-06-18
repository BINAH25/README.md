from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
