from django.db import models
from django.utils.timezone import now


class User(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    full_name = models.CharField(max_length=50, null=False)
    # username = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=False, unique=True, db_index=True)
    email = models.CharField(max_length=50, unique=True, null=False, db_index=True)
    password = models.CharField(max_length=250, null=False)
    # identityNumber = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10, null=False)
    address = models.CharField(default="", max_length=500, null=True)
    # salt = models.CharField(default="", max_length=100, null=False)
    # accessToken = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True, null=False)
    is_linked_to_dana = models.BooleanField(default=False, null=False)
    is_admin = models.BooleanField(default=False, null=False)
    created_by = models.BigIntegerField(null=True)
    updated_by = models.BigIntegerField(null=True)
    created_at = models.DateTimeField(null=False, default=now)
    updated_at = models.DateTimeField(null=False, default=now)

    class Meta:
        db_table = "users"
