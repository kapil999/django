from django.urls import path
from . import views
urlpatterns = [
    path('',views.listings,name='listings'),
    path('<uuid:id>',views.Listing_detail,name='listing'),
    #path('<Title>',views.Listing_name,name='Listing_name'),
    path('search/',views.search,name='search')
]