from django.test import SimpleTestCase
from django.urls import resolve
from app.views import *


class TestUrls(SimpleTestCase):
    def test_index_view(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_question_item(self):
        url = reverse('question', kwargs={'question_id': 1})
        self.assertEqual(resolve(url).func, question)

    def test_search_by_tags(self):
        url = reverse('search', kwargs={'tag_name': 'test'})
        self.assertEqual(resolve(url).func, search)

    def test_hot_questions(self):
        url = reverse('hot')
        self.assertEqual(resolve(url).func, show_hot)

    def test_ask_question(self):
        url = reverse('ask')
        self.assertEqual(resolve(url).func, ask)

    def test_login(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, log_in)

    def test_signup(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup)

    def test_logout(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

    def test_settings(self):
        url = reverse('settings')
        self.assertEqual(resolve(url).func, settings)

    def test_ratings(self):
        url = reverse('rate')
        self.assertEqual(resolve(url).func, rate)

    def test_correctness(self):
        url = reverse('correct')
        self.assertEqual(resolve(url).func, correct)
