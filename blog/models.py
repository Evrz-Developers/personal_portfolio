import datetime
from django.db import models


# Create your models here.
def get_default_created_at():
    now = datetime.datetime.now()
    adjusted_time = now + datetime.timedelta(hours=5, minutes=30)
    # formatted_time = adjusted_time.strftime("%I:%M %p | %d-%B-%Y")
    return adjusted_time


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(default=get_default_created_at)

    def __str__(self):
        return self.title
