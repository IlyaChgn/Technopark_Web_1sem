from django.db import models
from django.conf import settings
from django.db.models import Count

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True)
    login = models.CharField(max_length=30)


class Rating(models.Model):
    mark = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Tag(models.Model):
    tag = models.CharField(max_length=20)


class QuestionManager(models.Manager):
    def new_questions_list(self):
        return self.order_by('date').reverse()

    def hot_questions_list(self):
        return self.alias(c_rating=Сount('rating')).filter(c_rating__gt=90).order_by('-c_rating')

    def find_by_tag(self, tag_name):
        return self.prefetch_related('tags').filter(tags__tag=tag_name)


class Question(models.Model):
    def rating_count(self):
        return self.rating.count()

    def get_tags(self):
        tag_list = self.tags.all()
        tags = []
        for i in range(len(tag_list)):
            tags.append(tag_list[i].tag)
        return tags

    def answers_count(self):
        return Answer.objects.list_answers_count(self.pk)

    title = models.CharField(max_length=256)
    text = models.TextField()
    tags = models.ManyToManyField(Tag)
    date = models.DateTimeField()
    rating = models.ManyToManyField(Rating)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    objects = QuestionManager()


class AnswerManager(models.Manager):
    def list_answers_count(self, question_id):
        return self.filter(question=question_id).count()

    def answers_list(self, question_id):
        return self.filter(question=question_id).all()


class Answer(models.Model):
    def rating_count(self):
        return self.rating.count()

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField()
    rating = models.ManyToManyField(Rating)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    objects = AnswerManager()
