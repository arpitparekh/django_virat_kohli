from django.db import models

# mvt
# model view template

class EmailPassword(models.Model):
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
