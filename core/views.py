from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import Blog
from .forms import BlogForm


class Home(View):
	def get(self, request):
		context = {
			"blogs": Blog.objects.all().order_by("-id")[:3]
		}
		return render(request, "core/index.html", context)

class BlogView(View):
	def get(self, request):
		context = {
			"blogs": Blog.objects.all().order_by("-id")
		}
		return render(request, "core/blogs.html", context)
	
	def post(self, request):
		form = BlogForm(request.POST)
		if form.is_valid():
			blog = form.save()
			url = reverse("blog", args=[blog.slug])
			return redirect(url)
		return render(request, "core/add-blog.html")

class BlogDetail(View):
	def get(self, request, slug):
		context = {
			"blog": Blog.objects.get(slug=slug)
		}
		return render(request, "core/blog-detail.html", context)
