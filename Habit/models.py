from django.db import models

# Create your models here.
class Habit(models.Model):
	habit = models.TextField(null=True)
	Mon = models.TextField(null=True)
	Tue = models.TextField(null=True)
	Wed = models.TextField(null=True)
	Thu = models.TextField(null=True)
	Fri = models.TextField(null=True)
	Sat = models.TextField(null=True)
	Sun = models.TextField(null=True)
	Time = models.TextField(null=True)