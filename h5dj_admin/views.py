from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import django.contrib.auth
import rest_framework.viewsets
import serializers
import django.contrib.auth.models
import models


def check_user(user):
    if user is not None and user.is_active and user.is_authenticated():
            return True

    return False


def index(request):
    user = request.user
    if check_user(user):
        return render_to_response('index.html')

    return render_to_response('login.html')


def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    login(request, username, password)

    return HttpResponseRedirect('/')


def login(request, username, password):
    user = None
    try:
        user = django.contrib.auth.authenticate(username=username, password=password)
    except Exception, e:
        print Exception, ":", e

    if user is not None and user.is_active:
        django.contrib.auth.login(request, user)

    return user


def sign_out(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect('/')


class UserViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = django.contrib.auth.models.User.objects.all()
    serializer_class = serializers.UserSerializer


class StatisticsViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = models.Statistics.objects.all()
    serializer_class = serializers.StatisticsSerializer