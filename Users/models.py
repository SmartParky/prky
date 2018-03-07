from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
# Local Django
from Core.models import City

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError(_('Users must have email address.'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        if not email:
            raise ValueError(_('Admins must have email address.'))

        user = self.create_user(email,
            first_name=first_name,
            last_name=last_name)

        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    TYPE_CHOICES = (
        ('admin', _('Admin')),
        ('customer', _('Customer')),
        ('park-owner', _('Park Owner')),
    )

    email = models.EmailField(verbose_name=_('Email'), max_length=255,
                        unique=True)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
    phone_regex = RegexValidator(regex=r'^(05(\d{2}) (\d{3}) (\d{4}))$',
    message="Telefon numarası formatı şu şekilde olmalıdır: '05xx xxx xxxx'." )
    phone_number = models.CharField(verbose_name=_('Phone Number'),
    validators=[phone_regex], max_length=17) # validators should be a list

    city = models.ForeignKey(verbose_name=_('City'), to='Core.City', null=True)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    is_staff = models.BooleanField(verbose_name=_('Staff'), default=True)
    objects = UserManager()

    type = models.CharField(verbose_name=_('Type'), max_length=50, choices=TYPE_CHOICES, default="customer")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)

        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.get_full_name()
