from django.db import models

class RegisteredUser(models.Model):
    email = models.EmailField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    def __unicode__(self):
        return self.email

# Create your models here.
