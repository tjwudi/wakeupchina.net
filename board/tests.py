from django.test import TestCase

from .models import Post


class PostModelTest(TestCase):
    fixtures = ['initial_data']

    def test_str(self):
        """The __str__ method should return Post's title.
        """
        post = Post.objects.get(short_title="drive_less_walk_more")
        self.assertEqual(str(post), post.title)

    def test_as_json(self):
        """Should return a dict representation.
        """
        post = Post.objects.first()
        json = post.as_json()
        self.assertEqual(set(json.keys()), set([
            'description',
            'title',
            'short_title']))
