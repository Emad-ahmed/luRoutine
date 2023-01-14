from django.db import models
from core.models import AbstractTimestampModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class BindAccount(AbstractTimestampModel):
    class Roles(models.TextChoices):
        ADMIN = 'admin', _('Admin'),
        MEMBER = 'member', _('Member')
    user = models.OneToOneField(
        verbose_name=_('User'),
        to=User,
        related_name='bind_account',
        on_delete=models.CASCADE
    )
    teacher = models.OneToOneField(
        verbose_name=_('Teacher'),
        to='faculty.Teacher',
        related_name='bind_account',
        on_delete=models.CASCADE
    )
    role = models.CharField(
        verbose_name=_('Role'),
        choices=Roles.choices,
        max_length=8,
        default='member'
    )
