from django.test import TestCase

from .models import Post


class PostModelTest(TestCase):
    fixtures = ['initial_data']

    def test_pick_one_published(self):
        """Should return one Post object with `published=True`.
        """
        pass

    def test_str(self):
        """The __str__ method should return Post's title.
        """
        post = Post.objects.get(short_title="drive_less_walk_more")
        self.assertEqual(str(post), post.title)
