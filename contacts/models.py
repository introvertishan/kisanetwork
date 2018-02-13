from django.db import models
import datetime
# Create your models here.

# Initialising the models here
class Messages(models.Model):
    comment = models.TextField()
    Date_created = models.DateTimeField(auto_now_add=True,null=True)
    created_by = models.CharField(max_length=100, null=True)
    otp = models.IntegerField(null=True)

    class Meta:
        ordering = ['-Date_created']

    def __str__(self):
        return self.comment