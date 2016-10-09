"""
Definition of views.
"""
import urllib.request
import xml.etree.ElementTree
from math import radians, sin, atan2, sqrt, cos

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
    distance = request.GET.get('distance')
    print(request.GET)
    lat = request.GET.get('lat')
    print(lat)
    log = request.GET.get('lon')
    print(log)
    return {'result': True, 'conv': conv(root, distance, lat, log)}


def conv(xmlroot, distance, lat, log):
    r = []
    z_index = 0
    for i in xmlroot:
        if i.tag == 'DailyEarthquakes':
            e = [None, None, None, None, None, None, None, None]
            for j in i:
                if j.tag == 'OriginEnglish':
                    e[0] = j.text
                elif j.tag == 'Latitude':
                    e[1] = j.text
                elif j.tag == 'Longitude':
                    e[2] = j.text
                elif j.tag == 'DateTimeThai':
                    e[7] = j.text
                    print(e[3])
                elif j.tag == 'Depth':
                    e[4] = j.text
                elif j.tag == 'Magnitude':
                    e[5] = j.text
                elif j.tag == 'TitleThai':
                    e[6] = j.text
            if float(distance) >= calculate_distance(lat, log, e[1], e[2]):
                e[3] = z_index
                z_index += 1
                r.insert(len(r), e)
    return r


@ajax
@csrf_exempt
def fake_conv(request):
    r = []
    e = ['Bangkok', '13.813590', '99.959996', '0', '6', '4.5', 'กรุงเทพ', '2016-10-9']
    r.insert(len(r), e)
    print('======================================')
    return {'result': True, 'conv': r}


def calculate_distance(tlat1, tlon1, tlat2, tlon2):
    R = 6373.0

    lat1 = radians(float(tlat1))
    lon1 = radians(float(tlon1))
    lat2 = radians(float(tlat2))
    lon2 = radians(float(tlon2))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    print("Result:", distance)
    return distance