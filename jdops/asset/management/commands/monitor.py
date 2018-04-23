# coding: utf-8
from __future__ import unicode_literals

import json
import urllib2

from django.core.management.base import BaseCommand

from asset.models import Host, ResourceState
from code_scripts.collect_info import RemoteShell

class Command(BaseCommand):
    help = '监控资源'

    def handle(self, *args, **kwargs):
        """
        使用fabric接口操作状态为“使用中”的所有主机
        定时获取主机信息，如cpu，内存，硬盘等数据
        同时监控所有主机上服务的状态，主要是http服务是否可用
        """
        hosts = Host.objects.filter(status=2)
        '''select * from Host where status=2'''
        for host in hosts:
            remote = RemoteShell(host, host.username, host.password)
            result = {
                'cpu_load': remote.collect_cpu_load(),
                'free_mem': remote.collect_free_mem(),
                'disk_usage': remote.collect_disk_usage(),
                'services': [],
            }
            resource = ResourceState()
            resource.host = host
            resource.data = json.dumps(result)
            resource.save()
