from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Order)
admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Laptop)
admin.site.register(OrderItem)
admin.site.register(Reviews)