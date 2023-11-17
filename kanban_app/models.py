from django.db import models

# Create your models here.
class Column(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Card(models.Model):
    content = models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return self.content
