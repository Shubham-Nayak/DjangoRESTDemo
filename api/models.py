from django.db import models

# Create your models here.
class TblCommonmaster(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, blank=True)
    # imageurl = models.ImageField(upload_to='images/', blank=True, null=True)
    otherfield = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



