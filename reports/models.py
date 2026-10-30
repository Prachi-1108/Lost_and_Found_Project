from django.db import models

class LostFoundReport(models.Model):
  item_name = models.CharField(max_length=100)
  report_type = models.BooleanField(choices=[(True, 'Lost'), (False, 'Found')])
  description = models.TextField()
  location = models.CharField(max_length=100)
  date_reported = models.DateTimeField(auto_now_add=True)
  status = models.BooleanField(choices=[(True, 'Open'), (False, 'Resolved')])
  reported_by = models.ForeignKey(User, on_delete=models.CASCADE)