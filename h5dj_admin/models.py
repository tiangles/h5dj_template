from django.db import models


# class Admin(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField()
#     is_superuser = models.BooleanField()
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#     username = models.CharField(max_length=30)
#
#     class Meta:
#         db_table = "auth_user"


class Statistics(models.Model):
    new_order = models.IntegerField()
    new_visitors = models.IntegerField()
    new_user = models.IntegerField()
    profit_today = models.IntegerField()

    class Meta:
        db_table = "site_statistics"
