from django.core.management import BaseCommand

from app.views import cache_popular_tags


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        cache_popular_tags()
