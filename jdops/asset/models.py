# coding: utf-8
from __future__ import unicode_literals

from django.db import models

class HostGroup(models.Model):
    name = models.CharField(max_length=100, default="default", verbose_name="名称")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "主机组"



class Host(models.Model):
    STATUS_ITEMS = (
        (1, "未使用"),
        (2, "使用中"),
        (3, "已报废"),
    )
    name = models.CharField(max_length=100, blank=True, verbose_name="主机名")
    ip = models.GenericIPAddressField(verbose_name="主机IP")
    username = models.CharField(max_length=500, blank=True, verbose_name="主机用户名")
    password = models.CharField(max_length=500, blank=True, verbose_name="主机密码")
    
    group = models.ForeignKey(HostGroup, blank=True , verbose_name="所属主机组")

    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name="主机状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def icmp_monitor(self):
        ip = self.ip
        from code_scripts import ping
        temp = ping.ICMP_Monitor()
        return temp.verbose_ping(ip)

    icmp_monitor.admin_order_field = 'name'  # 根据什么字段排序
    icmp_monitor.boolean = True
    icmp_monitor.short_description = 'machine is on?'



    def __str__(self):
        return '<%s@%s>' % (self.username, self.ip)

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name_plural = "主机"


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="服务名称")
    url = models.CharField(max_length=500, blank=True, verbose_name="服务地址")
    ports = models.CharField(max_length=500, verbose_name="使用端口")
    contact = models.CharField(max_length=100, verbose_name="联系人")

    host = models.ForeignKey(Host, verbose_name="所属主机")
    
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    #def service_monitor(self):
        

    class Meta:
        verbose_name_plural = "服务"


