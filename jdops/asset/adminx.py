# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    Host, HostGroup, Service, ResourceState
)

import xadmin

from fabric.api import env, run
from code_scripts.collect_info import RemoteShell

# Register your models here.

class GlobalSettings(object):
    site_title = "京东云运维管理平台"
    site_footer = "imjerrychan.xyz"

def touch_file(object, request, queryset):
    for obj in queryset:   
        #import pdb; pdb.set_trace()
        ip, host, password = obj.ip, obj.username, obj.password
        RemoteShell(ip, host, password).touch_file()

class HostAdmin(object):
    list_display = ('name', 'group', 'ip', 'status', 'update_time', 'icmp_monitor')
    list_filter = ('name', 'group', 'status', 'created_time', 'update_time')
    search_fields = ('name', 'foreign_key_group')
    actions = [touch_file]

class HostGroupAdmin(object):
    list_display = ('name', 'created_time', 'update_time')
    list_filter = ('name', 'created_time')
    search_fields = ('name')

class ServiceAdmin(object):
    list_display = ('name', 'url', 'ports', 'host', 'update_time')
    list_filter = ('name', 'update_time', 'host')
    search_fields = ('name', 'url', 'host')


# 自定义页头页脚
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
# Model管理部分
xadmin.site.register(Host, HostAdmin)
xadmin.site.register(HostGroup, HostGroupAdmin)
xadmin.site.register(Service, ServiceAdmin)
xadmin.site.register(ResourceState)
