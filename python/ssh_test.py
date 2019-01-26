#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ssh_test
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/26
#    Change Activity:  2019/1/26:

import paramiko


cmd = "curl -s -o /tmp/authorized_keys  http://10.2.24.150:8000/client_key/authorized_keys"
host_info = "10.2.24.28"
cmd1 = "find /tmp/ -name authorized_keys"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host_info,port=22,username="root",password="playcrab")
stdin, stdout, stderr = ssh.exec_command(cmd)

stdin1, stdout2,stderr2= ssh.exec_command(cmd1)

stdout = stdout.read()
stderr = stderr.read()

stdout2 = stdout2.read()
stderr2 = stderr2.read()

print("stdout->",stdout)
print("stderr->",stderr)

print(stdout2)
print(stderr2)
ssh.close()

