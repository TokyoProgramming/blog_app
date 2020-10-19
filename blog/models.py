from django.db import models


class Blog(models.Model):
    title   =   models.CharField(max_length=30)
    text    =   models.TextField(max_length=200)
    date    =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



