from django.db import models

# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length=200,blank=False, unique=True)
	content = models.TextField()

	def __str__(self):
		return self.title
	