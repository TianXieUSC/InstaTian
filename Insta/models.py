from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField


class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profile',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )

    def get_connections(self):
        # search all the objects belonging to this class
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()


# define the model
class Post(models.Model):
    # define the user who post
    author = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='my_posts'
    )
    # defile textfile, can be posted with "blank" and "null".
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )

    def get_like_count(self):
        # related_name
        return self.likes.count()

    # once post has done, call this function, return to the post_detail html
    def get_absolute_url(self):
        # reverse function will go to urls.py to look for the url name
        return reverse("post_detail", args=[str(self.id)])


class Like(models.Model):
    # foreignkey pointing to another model
    post = models.ForeignKey(
        Post,
        # if the post is deleted, the relation is also deleted
        on_delete=models.CASCADE,
        # object can use 'object.like' to call
        related_name='likes'
    )
    user = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    # to define that the pair should be unique
    class Meta:
        unique_together = ("post", "user")

    # use this string to represent class
    def __str__(self):
        return 'Like: ' + self.user.username + ' likes ' + self.post.title


class UserConnection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    # following creator
    creator = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friendship_creator_set"
    )
    # following being followed
    following = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friend_set"
    )

    def __str__(self):
        return self.creator.username + ' follows ' + self.following.username


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE
    )
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment
