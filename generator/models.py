from django.db import models


class Profile(models.Model):
    email = models.EmailField()
    slug = models.CharField(unique=True, max_length=30)
    count = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
