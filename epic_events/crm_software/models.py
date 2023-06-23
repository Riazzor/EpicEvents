from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(UserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    first_name = models.CharField(verbose_name="Nom", max_length=25, blank=False)
    last_name = models.CharField(verbose_name="Prénom", max_length=25, blank=False)
    email = models.EmailField(verbose_name="Adresse email", blank=False, max_length=100, unique=True)
    username = None

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]


class Customer(models.Model):
    first_name = models.CharField(verbose_name="Nom", max_length=25, blank=False)
    last_name = models.CharField(verbose_name="Prénom", max_length=25, blank=False)
    email = models.EmailField(verbose_name="Adresse email", blank=False, max_length=100, unique=True)
    phone_number = PhoneNumberField(verbose_name="Numéro de fixe")
    mobile_number = PhoneNumberField(verbose_name="Numéro de portable")
    sales_member = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="customers",
    )
    company_name = models.CharField(verbose_name="Entreprise", max_length=250)
    date_created = models.DateTimeField(verbose_name="Date de création", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="Dernière mise à jour", auto_now=True)

    class Meta:
        verbose_name = 'Customer'


class Events(models.Model):
    class EventStatus(models.TextChoices):
        ON_GOING = "On_Going"
        FINISHED = "Finished"
    event_date = models.DateTimeField(verbose_name="Date de l'évènement")
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name="events")
    date_created = models.DateTimeField(verbose_name="Date de création", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="Dernière mise à jour", auto_now=True)
    support_member = models.ForeignKey(to=User, on_delete=models.SET_NULL, related_name="events", null=True)
    event_status = models.CharField(choices=EventStatus.choices, default=EventStatus.ON_GOING)
    attendees = models.IntegerField()

    @property
    def sales_member(self):
        return self.customer.sales_member


class Contract(models.Model):
    sales_member = models.ForeignKey(to=User, on_delete=models.SET_NULL, related_name="contracts", null=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name="contracts")
    status = models.BooleanField(verbose_name="Contrat terminé")
    amount = models.FloatField(verbose_name="Montant")
    payment_due = models.DateTimeField(verbose_name="Date de paiement")
    date_created = models.DateTimeField(verbose_name="Date de création", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="Dernière mise à jour", auto_now=True)
