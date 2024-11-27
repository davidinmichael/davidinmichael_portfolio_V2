from django.core.management.base import BaseCommand
from core.dummy_blogs import dummy_posts
from core.models import Blog


class Command(BaseCommand):
	help = "Command for creating dummy blogs"
	def handle(self, *args, **kwargs):
		for blog in dummy_posts:
			Blog.objects.create(title=blog["title"], body=blog["body"])