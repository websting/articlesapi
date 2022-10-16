from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=200, null=True)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.title