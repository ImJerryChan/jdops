# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    Host, HostGroup, Service, 
)

import xadmin
# Register your models here.

class GlobalSettings(object):
    site_title = "京东云运维管理平台"
    site_footer = "imjerrychan.xyz"

class HostAdmin(object):
    list_display = ('name', 'group', 'ip', 'status', 'update_time', 'icmp_monitor')
    list_filter = ('name', 'group', 'status', 'created_time', 'update_time')
    search_fields = ('name', 'foreign_key_group')

class HostGroupAdmin(object):
    list_display = ('name', 'created_time')
    list_filter = ('name', 'created_time')
    search_fields = ('name')

class ServiceAdmin(object):
    list_display = ('name', 'url', 'ports', 'update_time')
    list_filter = ('name', 'update_time')
    search_fields = ('name', 'url')


# 自定义页头页脚
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
# Model管理部分
xadmin.site.register(Host, HostAdmin)
xadmin.site.register(HostGroup, HostGroupAdmin)
xadmin.site.register(Service, ServiceAdmin)
