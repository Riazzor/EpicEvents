from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Contract, Customer, Events

User = get_user_model()

admin.site.register(User)
admin.site.register(Contract)
admin.site.register(Customer)
admin.site.register(Events)
