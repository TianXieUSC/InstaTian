from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
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

    # once post has done, call this function, return to the post_detail html
    def get_absolute_url(self):
        # reverse function will go to urls.py to look for the url name
        return reverse("post_detail", args=[str(self.id)])


class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profile',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )

