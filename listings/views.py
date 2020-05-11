from django.shortcuts import render, get_object_or_404
from . models import listing
from django.core.paginator import Paginator
from .choices import Bedroom_choices, Price_choices, State_choices
# Create your views here.
def listings(request):
	listings=listing.objects.all()
	paginator=Paginator(listings,3)
	Page=request.GET.get('page')
	listing_per_page=paginator.get_page(Page)
	context={'listings':listing_per_page}
	return render(request,'listings/listings.html',context)

def Listing_detail(request,id):
	Listing=get_object_or_404(listing,pk=id)
	Context={'listing':Listing}
	return render(request,'listings/listing.html',Context)

'''def Listing_name(request,Title):
    Listing=get_object_or_404(listing,Title=Title)
    Context={'listing':Listing}
    return render(request,'listings/listing.html',Context)'''
def search(request):
	listings=listing.objects.order_by('-Published_date')
	if 'keywords' in request.GET:
		keywords=request.GET['keywords']
		if keywords:
			listings=listings.filter(Aditional_details__icontains=keywords)
	if 'city' in request.GET:
	    city=request.GET['city']
	    if city:
	    	listings=listings.filter(City__iexact=city)
	if 'state' in request.GET:
	   	state=request.GET['state']
	   	if state:
	   		listings=listings.filter(State__iexact=state)
	if 'bedrooms' in request.GET:
	   	bedrooms=request.GET['bedrooms']
	   	if bedrooms:
	   		listings=listings.filter(Bedrooms__lte=bedrooms)
	if 'price' in request.GET:
	   	price=request.GET['price']
	   	if price:
	   		listings=listings.filter(Price__lte=price)
	Context={
	'listings': listings,
	'State_choices': State_choices,
	'Bedroom_choices':Bedroom_choices,
	'Price_choices':Price_choices,
	'values':request.GET
	}
	return render(request,'listings/search.html',Context)
   
	

