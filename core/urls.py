from django.urls import path
from .views import Home, BlogView, BlogDetail


urlpatterns = [
	path("", Home.as_view(), name="home"),
	path("blogs/", BlogView.as_view(), name="blogs"),
	path("blog/<str:slug>/", BlogDetail.as_view(), name="blog"),
]
