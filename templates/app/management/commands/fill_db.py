from django.core.management import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

from app.models import Profile, Rating, Tag, Question, Answer

fake = Faker()


class Command(BaseCommand):
    help = 'Filling Database'

    def add_arguments(self, parser):
        parser.add_argument("num", type=int)

    def handle(self, *args, **kwargs):
        num = kwargs['num']

        users = [
            User(
                username=fake.unique.user_name()[:fake.random_int(min=4, max=8)] + fake.unique.user_name()[
                                                                                   :fake.random_int(min=3, max=7)],
                email=fake.email(),
                password=fake.password(special_chars=False),
                first_name=fake.first_name(),
                last_name=fake.last_name()
            ) for i in range(num)
        ]
        User.objects.bulk_create(users)
        self.stdout.write("Finished with users")
        users = User.objects.all()

        profiles = [
            Profile(
                user=users[i],
                avatar=None,
                login=fake.first_name() + '_' + fake.last_name()
            ) for i in range(num)
        ]
        Profile.objects.bulk_create(profiles)
        self.stdout.write("Finished with profiles")
        profiles = Profile.objects.all()

        ratings = [
            Rating(
                mark=fake.random_int(min=0, max=10)
            ) for _ in range(num * 110)
        ]
        Rating.objects.bulk_create(ratings)
        ratings = Rating.objects.all()
        for r in ratings:
            k = r.mark
            unused_profiles = set()
            while k > 0:
                profile_num = fake.random_int(min=0, max=num - 1)
                if not (profile_num in unused_profiles):
                    k -= 1
                    unused_profiles.add(profile_num)
            unused_profiles = list(unused_profiles)
            r.profile.set([profiles[unused_profiles[i]] for i in range(len(unused_profiles))])
        self.stdout.write("Finished with ratings")
        ratings = Rating.objects.all()

        _tags = [
            Tag(
                tag=fake.word()
            ) for _ in range(num)
        ]
        Tag.objects.bulk_create(_tags)
        self.stdout.write("Finished with tags")
        _tags = Tag.objects.all()

        questions = [
            Question(
                title=fake.sentence(nb_words=fake.random_int(min=2, max=7)),
                text=fake.text(max_nb_chars=200),
                date=str(fake.date_time_this_decade()),
                profile=profiles[fake.random_int(min=0, max=num - 1)],
                rating=ratings[i]
            ) for i in range(num * 10)
        ]
        Question.objects.bulk_create(questions)
        questions = Question.objects.all()
        for q in questions:
            q.tags.set([_tags[fake.random_int(min=0, max=num - 1)] for _ in range(fake.random_int(min=1, max=5))])
        self.stdout.write("Finished with questions")

        answers = [
            Answer(
                question=questions[fake.random_int(min=0, max=num * 10 - 1)],
                text=fake.text(max_nb_chars=500),
                date=str(fake.date_time_this_decade()),
                profile=profiles[fake.random_int(min=0, max=num - 1)],
                is_correct=True if (fake.random_int() % 8 == 0) else False,
                rating=ratings[10 * num + i]
            ) for i in range(num * 100)
        ]
        Answer.objects.bulk_create(answers)
        self.stdout.write("Finished with answers")
