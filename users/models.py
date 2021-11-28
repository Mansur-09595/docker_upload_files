from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')

    # cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

