from django.db import models

# Create your models here.
class pms_db(models.Model):
	ip=models.CharField(max_length=20,unique=True)
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)


class pms_data(models.Model):
	ip_id=models.CharField(max_length=20)
	ram_usage=models.CharField(max_length=20)
	cpu_usage=models.CharField(max_length=20)
	mac_address = models.CharField(max_length=20)
	status=models.CharField(max_length=10)
	date_time=models.CharField(max_length=20)