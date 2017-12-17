import os
import paramiko 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.195.136', username="abc", password="1212")
sftp = ssh.open_sftp()
localpath = 'test1.txt'
remotepath = 'test.txt'
sftp.get('test.txt', 'download.txt')
sftp.close()
ssh.close()
