from datetime import datetime
from io import BytesIO
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models


def get_unique_filename(filename):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f'user_{timestamp}.jpg'


def compress(image):
    """
    Compresses the given image and returns a compressed image file.
    """
    im = Image.open(image)
    # Set the maximum size of the compressed image.
    max_size = (800, 800)
    im.thumbnail(max_size)
    # Save the compressed image to a BytesIO buffer.
    buffer = BytesIO()
    im.save(buffer, format='JPEG', quality=60)
    buffer.seek(0)
    # Return the compressed image file.
    return buffer


class CustomUser(AbstractUser):
    resume = models.FileField(upload_to='user/files/', blank=True)
    profile_picture = models.ImageField(upload_to='user/files/', blank=True)
    contact = models.CharField(max_length=15, blank=True)

    def save(self, *args, **kwargs):
        # Compress the image before saving.
        compressed_image = compress(self.profile_picture)
        self.profile_picture.save(
            get_unique_filename(self.profile_picture.name), compressed_image,
            save=False)
        super().save(*args, **kwargs)
