#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

from fabric.api import env, run

'''
Script to collect cpu_load, free_mem, dist_usage
Author: JerryChan
Date: 2018年4月18日13:16:49
'''

class RemoteShell(object):
    def __init__(self, ip, username='root', password=None):
        self.ip = ip
        self.username = username
        self.password = password

    def run(self, command):
        env.host_string = '%s@%s' % (self.username, self.ip)
        if self.password:
            env.password = self.password
        try:
            output = run(command, quiet=True)
        except Exception as e:
            return str(e)

        return output

    def collect_cpu_load(self):
        command = "uptime|awk '{print $8,$9,$10,$11,$12}'"
        return self.run(command)

    def collect_free_mem(self):
        command = "free -m"
        return self.run(command)
    
    def collect_disk_usage(self):
        command = "df -h"
        return self.run(command)

    def touch_file(self):
        command = "touch /tmp/temp/2.txt"
        return self.run(command)
