from django.shortcuts import render
from .models import Event

# Create your views here.
def details(request):
  return render(request, "events/details.html")

def events(request):
  events = Event.objects.all()
  return render(request, "events/events.html", {"events": events})

