from datetime import datetime, timedelta
from io import BytesIO
from PIL import Image
from django.db import models


def get_unique_filename(filename):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f'project_{timestamp}.jpg'


def compress(image):
    im = Image.open(image)
    max_size = (800, 800)
    im.thumbnail(max_size)
    buffer = BytesIO()
    im.save(buffer, format='JPEG', quality=60)
    buffer.seek(0)
    return buffer


def get_default_created_at():
    now = datetime.now()
    adjusted_time = now + timedelta(hours=5, minutes=30)
    return adjusted_time


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(default=get_default_created_at)
    skills = models.ManyToManyField('Skill', blank=True,
                                    related_name='projects')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Compress the image before saving.
        compressed_image = compress(self.image)
        self.image.save(get_unique_filename(self.image.name), compressed_image,
                        save=False)
        super().save(*args, **kwargs)


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE,
    #                             related_name='related_skills')

    def __str__(self):
        return self.name
