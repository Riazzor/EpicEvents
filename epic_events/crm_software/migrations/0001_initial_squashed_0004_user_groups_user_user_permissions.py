# Generated by Django 4.2.1 on 2023-06-06 20:06

import crm_software.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    replaces = [
        ("crm_software", "0001_initial"),
        ("crm_software", "0002_alter_user_options_remove_user_date_joined_and_more"),
        ("crm_software", "0003_user_is_active_user_is_staff_user_is_superuser"),
        ("crm_software", "0004_user_groups_user_user_permissions"),
    ]

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("first_name", models.CharField(max_length=25, verbose_name="Nom")),
                ("last_name", models.CharField(max_length=25, verbose_name="Prénom")),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="Adresse email"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", crm_software.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=25, verbose_name="Nom")),
                ("last_name", models.CharField(max_length=25, verbose_name="Prénom")),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="Adresse email"
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, verbose_name="Numéro de fixe"
                    ),
                ),
                (
                    "mobile_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, verbose_name="Numéro de portable"
                    ),
                ),
                (
                    "company_name",
                    models.CharField(max_length=250, verbose_name="Entreprise"),
                ),
                (
                    "sales_team",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="customers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Customer",
            },
        ),
        migrations.CreateModel(
            name="Events",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.IntegerField(verbose_name="Prix")),
                (
                    "event_date",
                    models.DateTimeField(verbose_name="Date de l'évènement"),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date de création"
                    ),
                ),
                (
                    "date_updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Dernière mise à jour"
                    ),
                ),
                ("manufacturer", models.CharField()),
                ("type", models.IntegerField()),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="crm_software.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(verbose_name="Contrat terminé")),
                ("amount", models.FloatField(verbose_name="Montant")),
                ("payment_due", models.DateTimeField(verbose_name="Date de paiement")),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="crm_software.customer",
                    ),
                ),
                (
                    "sales_team",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="contracts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
