from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"Category: {self.name} Description: {self.description}"

class Post(models.Model):
    title = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=128)

    def __str__(self):
        return f"Title: {self.title} Content: {self.content}"