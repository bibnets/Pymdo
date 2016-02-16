#!/usr/bin/python
from fabric.api import *

env.user='root'
env.hosts='10.10.254.51'
env.password='@ug6tso'

@runs_once
def local_task():
	local("uname -a")
	
def remote_task():
	with cd("/code"):
		run("ls -l")
