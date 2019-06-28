from django.db import models
from datetime import datetime

class Issue(models.Model):
	title = models.CharField(max_length=200)
	desc = models.CharField(max_length=600)
	created = models.DateTimeField('date/time created', default=datetime.now)
	status = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class TimeEntry(models.Model):
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	desc = models.CharField(max_length=600)
	start = models.DateTimeField('date/time created')
	end = models.DateTimeField('date/time created', default=datetime.now)

	def __str__(self):
		return self.desc
