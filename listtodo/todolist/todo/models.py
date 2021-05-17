from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo (models.Model):
    title = models.CharField(max_length=255)
    memo= models.TextField(blank=True) #не обязательно к заполнению
    date_created=models.DateTimeField(auto_now_add=True)
    date_comleted=models.DateTimeField(null=True, blank=True)
    imported=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title