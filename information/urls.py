from . import views
from django.urls import path

urlpatterns = [
  path("", views.home, name="information_home"),
  path("django_meetup/", views.django_meetup, name="django_meetup")
]