from django.shortcuts import render, get_object_or_404
from .models import Event

# Create your views here.
def events(request):
  events = Event.objects.all()
  return render(request, "events/events.html", {"events": events})


def details(request, id):
  eventFromDB = get_object_or_404(Event, id = id)
  return render(request, "events/details.html", {"event": eventFromDB})
  
