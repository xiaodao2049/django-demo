from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age=models.IntegerField(max_length=3)
    gender = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    date=models.DateField(default='2018-5-2')
    writer=models.ForeignKey('Author',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
