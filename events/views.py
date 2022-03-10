from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event

# Create your views here.
def events(request):

  filter_map = {
    "title": "title__icontains",
    "is_free": "cost__exact"
  }

  filters = {}

  for key, value in request.GET.items():
        filter_key = filter_map[key]
        if value:
            filters[filter_key] = value

  events = Event.objects.filter(**filters)
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
  
