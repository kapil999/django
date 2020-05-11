from django.db import models
from realtors.models import Realtor
from datetime import datetime
import uuid
from .choices import STATE
# Create your models here.
class listing(models.Model):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	Realtor_Name=models.ForeignKey(Realtor,on_delete=models.CASCADE)
	Title=models.CharField(max_length=50)
	Aditional_details=models.TextField()
	Zip=models.CharField(max_length=100)
	Address=models.CharField(max_length=100)
	City=models.CharField(max_length=100)
	State=models.CharField(max_length=20,choices=STATE)
	Sqft=models.IntegerField()
	Lot_size=models.IntegerField()
	Published_date=models.DateTimeField(default=datetime.now)
	Bedrooms=models.IntegerField()
	Bathrooms=models.IntegerField()
	Garage=models.IntegerField(default=0)
	Price=models.CharField(max_length=100)
	Main_photo=models.ImageField(upload_to='image')
	Optional_photos1=models.ImageField(upload_to='image',blank=True, null=True, default="default.png")
	Optional_photos2=models.ImageField(upload_to='image',blank=True, null=True, default="default.png")
	Optional_photos3=models.ImageField(upload_to='image',blank=True, null=True, default="default.png")
	Optional_photos4=models.ImageField(upload_to='image',blank=True, null=True, default="default.png")
	Optional_photos5=models.ImageField(upload_to='image',blank=True, null=True, default="default.png")
	Optional_photos6=models.ImageField(upload_to='image',blank=True, null=True, default="default.png")
	Age_of_Property=models.IntegerField()
	Main_enterance_facing=models.CharField(max_length=50)
	