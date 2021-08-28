from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=False)
    completed = models.BooleanField(blank=False, null=False, default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    #created_on = models.DateTimeField(auto_now_add=True)
    #update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return"{}".format(self.title)
