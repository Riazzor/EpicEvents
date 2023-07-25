from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UA
from django.utils.translation import gettext_lazy as _
from .models import Contract, Customer, Events

User = get_user_model()


@admin.register(User)
class UserAdmin(UA):
    list_display = (
        "first_name",
        "last_name",
        "email",
    )
    search_fields = (
        "first_name",
        "last_name",
    )
    ordering = ('last_name',)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name", "password1", "password2", "groups"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("password",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("first_name", "last_name", "email")


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sales_member":
            kwargs["queryset"] = User.objects.filter(groups__name__in=['sales'])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sales_member":
            kwargs["queryset"] = User.objects.filter(groups__name__in=['sales'])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "support_member":
            kwargs["queryset"] = User.objects.filter(groups__name__in=["support"])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
