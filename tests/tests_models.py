from datetime import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model
from app.models import Question, Answer, Tag, Profile, QuestionRating, AnswerRating

User = get_user_model()


class QuestionModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='secret')
        self.profile = Profile.objects.create(user=self.user)
        self.question = Question.objects.create(profile=self.profile, title='Test Question', text='Test Body',
                                                date=datetime.now())

    def test_tags_list(self):
        tag1 = Tag.objects.create(tag='tag1')
        tag2 = Tag.objects.create(tag='tag2')
        self.question.tags.add(tag1, tag2)
        tags_list = self.question.get_tags()
        self.assertEqual(len(tags_list), 2)
        self.assertIn(tag1.tag, tags_list)
        self.assertIn(tag2.tag, tags_list)

    def test_rating_count(self):
        QuestionRating.objects.create(profile=self.profile, post=self.question, mark=1)
        self.assertEqual(self.question.rating_count(), 1)

    def test_answers_count(self):
        Answer.objects.create(profile=self.profile, question=self.question, text='Answer 1', date=datetime.now())
        Answer.objects.create(profile=self.profile, question=self.question, text='Answer 2', date=datetime.now())
        self.assertEqual(self.question.answers_count(), 2)

    def test_negative_votes(self):
        QuestionRating.objects.create(profile=self.profile, post=self.question, mark=-1)
        self.assertIn(self.profile, self.question.get_negative_votes())

    def test_positive_votes(self):
        QuestionRating.objects.create(profile=self.profile, post=self.question, mark=1)
        self.assertIn(self.profile, self.question.get_positive_votes())

class AnswerModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='secret')
        self.profile = Profile.objects.create(user=self.user)
        self.question = Question.objects.create(profile=self.profile, title='Test Question', text='Test Body',
                                                date=datetime.now())
        self.answer = Answer.objects.create(profile=self.profile, question=self.question, text='Test Answer',
                                            date=datetime.now())

    def test_rating_count(self):
        AnswerRating.objects.create(profile=self.profile, post=self.answer, mark=1)
        self.assertEqual(self.answer.rating_count(), 1)

    def test_negative_votes(self):
        AnswerRating.objects.create(profile=self.profile, post=self.answer, mark=-1)
        self.assertIn(self.profile, self.answer.get_negative_votes())

    def test_positive_votes(self):
        AnswerRating.objects.create(profile=self.profile, post=self.answer, mark=1)
        self.assertIn(self.profile, self.answer.get_positive_votes())


class TagModelTests(TestCase):
    def test_create_tag(self):
        tag = Tag.objects.create(tag='Test Tag')
        self.assertEqual(tag.tag, 'Test Tag')


class ProfileModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='secret')
        self.profile = Profile.objects.create(user=self.user)

    def test_profile_user(self):
        self.assertEqual(self.profile.user, self.user)

    def test_profile_avatar(self):
        self.assertEqual(self.profile.avatar.name, 'default.png')
