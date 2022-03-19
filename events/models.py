from django.db import models

class Event(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
  cost = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return self.title

class Review(models.Model):
  profile = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE, related_name="event_reviews")
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_reviews")
  rating = models.IntegerField()
  text = models.TextField()
