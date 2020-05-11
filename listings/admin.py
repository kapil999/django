from django.contrib import admin
from .models import listing
# Register your models here.
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
	list_filter=('Title','Realtor_Name',)
	search_fields=('Realtor_Name','Title','Zip',)
	list_display=('Title','Published_date','Realtor_Name',)
admin.site.register(listing,ListingAdmin)