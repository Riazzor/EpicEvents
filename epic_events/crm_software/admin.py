from django.contrib import admin
from .models import User, Contract, Customer, Events


admin.site.register(User)
admin.site.register(Contract)
admin.site.register(Customer)
admin.site.register(Events)
