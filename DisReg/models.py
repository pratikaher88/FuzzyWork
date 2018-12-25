from django.db import models

class UserInputValues(models.Model):
	
	Location = models.CharField(max_length=100)
	Kind_of_info = models.CharField(max_length=100)
	Criticality = models.CharField(max_length=100)

	def __str__(self):
		return self.Location
