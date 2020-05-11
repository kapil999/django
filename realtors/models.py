from django.db import models

# Create your models here.
class Realtor(models.Model):
	First_Name=models.CharField(max_length=200)
	Last_Name=models.CharField(max_length=200)
	Picture=models.ImageField(upload_to='image')
	Mobile_No=models.CharField(max_length=100)
	Email=models.EmailField()
	Experience=models.CharField(max_length=100)

	def __str__(self):
		return self.First_Name+' '+self.Last_Name
