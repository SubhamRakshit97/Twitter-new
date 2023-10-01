from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Tweet(models.Model):
    class Meta(object):
        db_table = 'Tweet'

    name = models.CharField(max_length= 40,db_index=True)
    body = models.CharField(max_length = 40,db_index=True)
    image = CloudinaryField(
        blank=True, null= True
    )
    like = models.IntegerField(
        default=0, blank=True, null=True
    )
    unlike = models.IntegerField(
        default=0, blank=True, null=True
    )
    created_at = models.DateTimeField(
            auto_now = True
        )

    def __str__(self): 
        return self.name