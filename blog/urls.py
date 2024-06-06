from django.urls import path
from dtech_hub import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("contact/", views.blog_contact, name="blog_contact"),
    path("about/", views.blog_about, name="blog_about"),
    path("about/dev-bio", views.blog_dev_bio, name="blog_dev_bio"),
    path("success/", views.success, name="success"),
    path("search/", views.blog_search, name="blog_search"),
]