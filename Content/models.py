from django.db import models

# Create your models here.

class Content(models.Model):
    attraction_name = models.CharField(max_length=255)
    description = models.TextField()
    is_landmark = models.BooleanField(default=False)

    def __str__(self):
        return self.attraction_name