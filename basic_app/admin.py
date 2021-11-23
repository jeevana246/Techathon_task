from django.contrib import admin
from basic_app.models import customers,producers,Retailers
# Register your models here.
admin.site.register(customers)
admin.site.register(producers)
admin.site.register(Retailers)