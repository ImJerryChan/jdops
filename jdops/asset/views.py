# coding: utf-8
from __future__ import unicode_literals

from django.shortcuts import render_to_response

from models import Host
def index(request):
    return render_to_response('index.html', {})


def menu(request):
    return render_to_response('menu.html', {})


def test(request):
    hosts = Host.objects.filter(status=2)
    return render_to_response('test.html', {'hosts': hosts})


def monitor(request):
    return render_to_response('monitor.html', {})
