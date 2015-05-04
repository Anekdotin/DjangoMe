from django.db import models


class Join(models.Model):

    email = models.EmailField(unique=True)
    ip_address = models.CharField(max_length=120, default='ABC')

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)



    def __unicode__(self):
        return "%s" %(self.email)
