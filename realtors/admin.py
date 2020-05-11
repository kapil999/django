from django.contrib import admin
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
	list_filter=('First_Name','id')
	search_fields=('id','First_Name',)
admin.site.register(Realtor,RealtorAdmin)