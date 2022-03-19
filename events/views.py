from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Event, Review
from accounts.models import UserProfile

# Create your views here.
def get_user_profile(request):
  if request.user.is_authenticated:
    [profile, created] = UserProfile.objects.get_or_create(user=request.user)
    return profile


def events(request):
  today = datetime.today()

  filter_map = {
    "title": "title__icontains",
    "is_free": "cost__exact"
  }

  filters = {}

  for key, value in request.GET.items():
    filter_key = filter_map[key]
    if value:
      filters[filter_key] = value

  events = Event.objects.filter(datetime__gte=today).filter(**filters).order_by("datetime")
  return render(request, "events/events.html", {"events": events})

@login_required
def add_attending(request, id):
  event = get_object_or_404(Event, id=id)
  if request.method == "POST":
    request.user.profile.attending.add(event)
  return redirect("events_list")


@login_required
def remove_attending(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        request.user.profile.attending.remove(event)
    return redirect("events_list")


def details(request, id):
  eventFromDB = get_object_or_404(Event, id = id)
  return render(request, "events/details.html", {"event": eventFromDB})


def dashboard(request):
  today = datetime.today()

  filters = {}
  
  user_profile = get_user_profile(request)
  future_attend = user_profile.attending.filter(datetime__gte=today).filter(**filters).order_by("datetime")
  past_attend = user_profile.attending.filter(datetime__lte=today).filter(**filters).order_by("datetime")
  return render(request, "events/dashboard.html", {"future": future_attend, "past": past_attend})
  
def new_review(request, id):
  event = get_object_or_404(Event, id=id)
  if request.method == "POST":
    rating = request.POST["rating"]
    text = request.POST["text"]
    new_review = Review(
      rating = rating,
      text = text,
      event = event,
      profile = get_user_profile(request)
    )
    new_review.save()
    return redirect("/events")