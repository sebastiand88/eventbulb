from django.shortcuts import render, get_object_or_404
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


def details(request, id):
  eventFromDB = get_object_or_404(Event, id = id)
  return render(request, "events/details.html", {"event": eventFromDB})
  
