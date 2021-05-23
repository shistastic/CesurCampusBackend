from django.db import models

# Create your models here.
class ContentFile(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='content/', default='-')