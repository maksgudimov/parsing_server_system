from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=128, blank=True, null=True)
    is_system = models.BooleanField(default=False)
    phone = PhoneNumberField(
        blank=True,
        null=True,
        default=None,
        unique=True,
        db_index=True
    )
    unique_id = models.CharField(max_length=32, unique=True, blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='account_user_groups',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='account_user_permissions',
        blank=True
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        permissions = [
            (
                "can_send_integration_requests",
                "Can send integration requests",
            ),
        ]

    def __str__(self):
        return self.name

