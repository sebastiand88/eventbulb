from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, "information/home.html")

def django_meetup(request):
  return render(request, "information/django_meetup.html")