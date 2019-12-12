from django.db import models
from imagekit.models import ProcessedImageField


# define the model
class Post(models.Model):
    # defile textfile, can be posted with "blank" and "null".
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )
