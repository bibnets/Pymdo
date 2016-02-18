#!/usr/bin/python
import paramiko

hostname='your ip here'
username='your username here'
password='your password here'
paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('sh ip route')
print stdout.read()
ssh.close()
