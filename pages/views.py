from django.shortcuts import render
from listings.models import listing
from listings.choices import Bedroom_choices, Price_choices, State_choices
# Create your views here.
def home(request):
	latest_listings=listing.objects.order_by('-Published_date')[ :3]
	cotext={
	'latest_listings':latest_listings,
	'State_choices': State_choices,
	'Bedroom_choices':Bedroom_choices,
	'Price_choices':Price_choices
	}
	return render(request,'pages/index.html',cotext)

def about(request):
	
	return render(request,'pages/about.html')
	

			