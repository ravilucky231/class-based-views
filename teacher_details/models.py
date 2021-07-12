from django.db import models
from django.urls import reverse


class Teachers(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    address=models.TextField()
    contact=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('teachers_index')

# Create your models here.
