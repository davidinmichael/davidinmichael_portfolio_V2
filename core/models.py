from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Blog(models.Model):
	title = models.CharField(max_length=50)
	body = models.TextField()
	picture = models.ImageField(upload_to="blogs/", default="blogs/blog.jpg")
	date_added = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	is_published = models.BooleanField(default=True)
	added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	slug = models.SlugField()
	excerpt = models.TextField()

	def __str__(self):
		return f"{self.title} | {self.added_by.first_name}"
	
	def save(self, *args, **kwargs):
		if not self.slug:
			base_slug = slugify(self.title)
			self.slug = f"{base_slug}-{self.id}" if self.id else base_slug
		if not self.excerpt:
			self.excerpt = ' '.join(self.body.split()[:50])
		return super().save(*args, **kwargs)
