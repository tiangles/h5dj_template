from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import django.contrib.auth
import rest_framework.viewsets
import rest_framework.generics
import serializers
import django.contrib.auth.models
import models


def login_required(func):
    def _deco(request):
        user = request.user
        if user is not None and user.is_active and user.is_authenticated():
            return func(request)
        else:
            return render_to_response('login.html')
    return _deco


@login_required
def dashboard(request):
    return render_to_response('index.html')


@login_required
def grids(request):
    return render_to_response('grids.html')


@login_required
def inbox(request):
    return render_to_response('inbox.html')


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


# class EmailInboxViewSet(rest_framework.generics.RetrieveUpdateDestroyAPIView):
class EmailInboxViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = models.EmailEntity.objects.all()
    serializer_class = serializers.EmailEntitySerializer
