import datetime

from datetime import datetime
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from app.models import Profile, Tag
from app.views import *


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class SearchTagsViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.profile = Profile.objects.create(user=self.user)

    def test_tag_view(self):
        tag = Tag.objects.create(tag='test_tag')
        question_ = Question.objects.create(profile=self.profile, title='Test Question', text='Test Body',
                                            date=datetime.now())
        question_.tags.add(tag)
        request = self.factory.get(reverse('search', kwargs={'tag_name': tag.tag}))
        request.user = self.user
        response = search(request, tag.tag)
        self.assertEqual(response.status_code, 200)


class HotViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hot_view(self):
        response = self.client.get(reverse('hot'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class QuestionViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com',
                                                         password='secret')
        self.profile = Profile.objects.create(user=self.user)
        self.question = Question.objects.create(profile=self.profile, title='Test Question',
                                                text='This is a test question', date=datetime.now())

    def test_logged_in_user_view(self):
        request = self.factory.get(reverse('question', kwargs={'question_id': self.question.pk}))
        request.user = self.user
        response = question(request, self.question.pk)
        self.assertEqual(response.status_code, 200)

    def test_logged_out_user_view(self):
        request = self.factory.get(reverse('question', kwargs={'question_id': self.question.pk}))
        request.user = AnonymousUser()
        response = question(request, self.question.id)
        self.assertEqual(response.status_code, 200)

    def test_post_new_answer(self):
        request = self.factory.post(reverse('question', kwargs={'question_id': self.question.pk}),
                                    {'text': 'Test answer body'})
        request.user = self.user
        response = question(request, self.question.id)
        self.assertEqual(response.status_code, 403)

    def test_post_empty_answer(self):
        request = self.factory.post(reverse('question', kwargs={'question_id': self.question.pk}), {'text': ''})
        request.user = self.user
        response = question(request, self.question.pk)
        self.assertEqual(response.status_code, 403)


class AskViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com',
                                                         password='secret')
        self.profile = Profile.objects.create(user=self.user)
        self.client.login(username='testuser', password='secret')

    def test_get_ask_view(self):
        request = self.factory.get(reverse('ask'))
        request.user = self.user
        response = ask(request)
        self.assertEqual(response.status_code, 200)

    def test_post_ask_view_valid_form(self):
        data = {
            'title': 'Test Question',
            'text': 'Test Body Test BodyTest BodyTest BodyTest BodyTest BodyTest',
            'tags': 'tag1, tag2'
        }
        response = self.client.post(reverse('ask'), data=data)
        question_ = Question.objects.get(title='Test Question')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('question', args=[question_.id]))

    def test_post_ask_view_invalid_form(self):
        data = {
            'title': 'Test Question',
            'text': 'Test Body',
            'tags': '!!@#'
        }
        response = self.client.post(reverse('ask'), data=data)
        self.assertEqual(response.status_code, 200)
