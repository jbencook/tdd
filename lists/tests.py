from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        # Exercise
        found = resolve('/')

        # Assert
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # Setup
        request = HttpRequest()
        response = home_page(request)

        # Exercise
        expected_html = render_to_string('home.html')

        # Assert
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        # Setup
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        # Exercise
        response = home_page(request)

        # Assert
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'}
        )
        self.assertEqual(response.content.decode(), expected_html)


