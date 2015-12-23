from django.db import models


class Post(models.Model):
    # Description of this post
    description = models.TextField()
    # Is this post published or not?
    # Not-published post will not be picked by random algorithm.
    published = models.BooleanField(default=False)
    # A url-friendly short title, good for SEO reason.
    short_title = models.CharField(
        max_length=100,
        unique=True)
    # Title of this post.
    # It's generally a call for action like "Drive less, walk more".
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def as_json(self):
        """Returns JSON representation of the Post.
        """
        return {
            'title': self.title,
            'short_title': self.short_title,
            'description': self.description,
        }
