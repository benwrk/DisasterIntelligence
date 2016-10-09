"""
Definition of urls for DisasterIntelligence.
"""

from datetime import datetime

from app import views
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views


urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^get_lat_lon/$', views.get_lat_lon, name='get_lat_lon'),
    url(r'^fake_conv/$', views.fake_conv, name='fake_conv'),
]
