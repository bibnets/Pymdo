#!/usr/bin/python
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user='root'
env.hosts='10.10.254.51'
env.password='abc'

@task
@runs_once
def tar_task():
	with cd("/home/oracle"):
		run("tar -czvf p1.tar.gz p1.dmp")

@task
def get_task():
	with lcd("/home/received"):
		get("/home/oracle/p1.tar.gz", "./p1.tar.gz")

@task
def untar_task():
	with lcd("/home/received"):
		local("tar -zxvf p1.tar.gz")

@task
def go():
	tar_task()
	get_task()
	untar_task()

