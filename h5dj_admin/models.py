from django.db import models
import django.contrib.auth.models


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
        db_table = "admin_site_statistics"


class EmailEntity(models.Model):
    user = models.ForeignKey(django.contrib.auth.models.User, related_name='email_owner')
    #MIME header
    mime_from = models.EmailField(max_length=128)
    mime_to = models.CharField(max_length=128)
    mime_cc = models.CharField(max_length=128)
    mime_bcc = models.CharField(max_length=128)
    mime_date = models.DateTimeField()
    mime_subject = models.CharField(max_length=128)
    mime_transfer_encoding = models.CharField(max_length=8)
    #MIME content
    content_type = models.CharField(max_length=8)

    class Meta:
        db_table = "admin_email_inbox"
