from . import views
from django.urls import path

urlpatterns = [
  path("", views.events, name="events_list"),
  path("details/", views.details, name="events_details")
]