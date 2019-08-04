import sqlite3
import django
import os
import paramiko
import sys
from datetime import datetime
sys.path.append("C:/Users/ashis/OneDrive/Desktop/PMS")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PMS.settings')
django.setup()


from django.contrib.auth.models import User
from myapp.models import pms_db as Client
from myapp.models import pms_data as Client_data

field_name_list = ['ip', 'username', 'password']
allClients = Client.objects.all()
authentication_data = []
for key in allClients:
        results = []
        for field_name in field_name_list:
                field_object = Client._meta.get_field(field_name)
                field_value = field_object.value_from_object(key)
                results.append(field_value)
        authentication_data.append(results)

print(authentication_data)
for each_user in authentication_data:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
        client.connect(each_user[0], username=each_user[1], password=each_user[2])
        stdin, cpu, stderr = client.exec_command('top -b -d1 -n1|grep -i \'Cpu(s)\'|head -c21|cut -d \' \' -f3|cut -d \'%\' -f1')
        stdin, top5, stderr = client.exec_command(' ps ahux --sort=-c | awk \'NR<=5{printf\" %s\\n\",$11}\'')
        stdin, ram, stderr = client.exec_command('free | grep Mem | awk \'{print $3/$2 * 100.0}\'')
        stdin, mac, stderr = client.exec_command('nmcli device show wlan0 | grep GENERAL.HWADDR | cut -c41-')
        for cpu_value in cpu:
                cpu_data = cpu_value
        for ram_value in ram:
                print(ram_value)
                ram_data = ram_value
        for mac_value in mac:
                print(mac_value)
                mac_data = mac_value
        new_data = Client_data(ip_id=each_user[0], ram_usage=ram_data, cpu_usage=cpu_data, mac_address=mac_data, status='Active', date_time=datetime.now())
        new_data.save()
        client.close()
