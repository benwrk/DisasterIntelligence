"""
Definition of views.
"""
import urllib.request
import xml.etree.ElementTree

from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from django_ajax.decorators import ajax
from collections import defaultdict

from django.views.decorators.csrf import csrf_exempt

seismic_feed_api = 'http://data.tmd.go.th/api/DailySeismicEvent/v1/?uid=api&ukey=api12345'


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


@ajax
@csrf_exempt
def get_lat_lon(request):
    f = urllib.request.urlopen(seismic_feed_api).read()
    root = xml.etree.ElementTree.fromstring(f)
    return {'result': True, 'conv': conv(root)}


def conv(xmlroot):
    r = []
    z_index = 0
    for i in xmlroot:
        if i.tag == 'DailyEarthquakes':
            e = [None, None, None, None]
            for j in i:
                if j.tag == 'OriginEnglish':
                    e[0] = j.text
                elif j.tag == 'Latitude':
                    e[1] = j.text
                elif j.tag == 'Longitude':
                    e[2] = j.text
            e[3] = z_index
            z_index += 1
            r.insert(len(r), e)
    return r