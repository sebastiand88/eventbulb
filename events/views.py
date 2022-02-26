from django.shortcuts import render

# Create your views here.
def details(request):
  return render(request, "events/details.html")

def events(request):
  return render(request, "events/events.html")