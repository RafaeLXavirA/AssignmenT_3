import os
import paramiko 

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('fe80::20c:29ff:fe44:7677%eth0', username="abc", password="1212")

sftp = ssh.open_sftp()
sftp.get('test.txt', 'download.txt')
sftp.close()
ssh.close()
