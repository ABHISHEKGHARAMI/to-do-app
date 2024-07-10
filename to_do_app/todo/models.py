from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]
        
    def __str__(self):
        return self.title
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    
    
    def __str__(self):
        return self.user.username
    