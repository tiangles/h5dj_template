"""h5dj_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
import h5dj_admin.views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', h5dj_admin.views.UserViewSet)
router.register(r'statistics', h5dj_admin.views.StatisticsViewSet)


urlpatterns = [
    url(r'^$', h5dj_admin.views.dashboard, name='index'),
    url(r'^dashboard$', h5dj_admin.views.dashboard, name='dashboard'),
    url(r'^inbox$', h5dj_admin.views.inbox, name='inbox'),
    url(r'^grids$', h5dj_admin.views.grids, name='grids'),
    url(r'^authenticate$', h5dj_admin.views.authenticate, name='authenticate'),
    url(r'^sign-out$', h5dj_admin.views.sign_out, name='sign_out'),
    url(r'^api/', include(router.urls)),
]
