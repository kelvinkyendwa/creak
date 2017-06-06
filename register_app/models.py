from django.db import models

# Create your models here.

class FirstName(model.Model):
    first_name = model.CharField(max_length=264)

    def __str__(self):
        return self.FirstName
