from django.shortcuts import render
import psutil
import socket
from django.http import HttpResponse
from .models import pms_db ,pms_data

import datetime
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout


def home(request):
    return redirect('/login/?next=%s' % request.path)
	
def get_final_data():
	all_ip=[]
	all_db=pms_db.objects.all()
	for db in all_db:
		all_ip.append(db.ip)
	print(all_ip)
	all_data=pms_data.objects.all().order_by('-id')[:80]
	print(all_data)
	final_data=[]
	for ip in all_ip:
		for db in all_data:
			if ip==db.ip_id:
				final_data.append(db)
				break
	print(final_data)
	return final_data
	
	
def hello(request):

	#content = { "cpu_percent" : psutil.cpu_percent(interval=1),
	#			"cpu_times" : psutil.cpu_times(),
	#			"memory_stats" : psutil.virtual_memory()
	#		}
	#return render(request, "hello.html",{ "context" : content})
	if request.user.is_authenticated:
	    final_data=get_final_data()
	    return render(request,"nodes.html",{"final_data":final_data}) 
	if not request.user.is_authenticated:
	    return redirect('/login/?next=%s' % request.path)		
    


def adduser(request):
    if not request.user.is_authenticated:
	    return redirect('/login/?next=%s' % request.path)
    if request.user.is_authenticated:
	    return render(request,"adduser.html",{})
			
    

	

#on successful additon of any node
def success(request):
    if not request.user.is_authenticated:
	    return redirect('/login/?next=%s' % request.path)
    if request.user.is_authenticated:
	    ip=request.POST["node_ip"]
	    username=request.POST["username"]
	    password=request.POST["password"]
	    a=pms_db(ip=ip,username=username, password=password)
	    a.save()
	    return render(request,"success.html",{})		

# Redirect to deleteuser page
def deleteuser(request):
    if not request.user.is_authenticated:
	    return redirect('/login/?next=%s' % request.path)
    if request.user.is_authenticated:
	    return render(request,"deleteuser.html",{})		


# To delete particular node by node_id
def delete(request):
    if not request.user.is_authenticated:
	    return redirect('/login/?next=%s' % request.path)
    if request.user.is_authenticated:
	    ip=request.POST["ip"]
	    pms_db.objects.filter(ip=ip).delete()
	    return render(request,"delete.html",{})
	
	

	
# To show Table
def table(request):
    if not request.user.is_authenticated:
	    return redirect('/login/?next=%s' % request.path)
    if request.user.is_authenticated:
	    final_data=get_final_data()		
	    return render(request,"table.html",{"final_data":final_data}) 	

			
'''
def logout(request):
    print("done")
    request.session['username'] = None
    request.session['password'] = None
    return redirect('login')
	
'''	
def chart(request):
	final_data=get_final_data()	
	return render(request,"chart.html",{"final_data":final_data})





def load_chart(request): 
	final_data=get_final_data()

	return render(request,"load_chart.html",{"final_data":final_data})





def load_nodes(request): 
	final_data=get_final_data()
	return render(request,"load_nodes.html",{"final_data":final_data})
	# return render(request,"load_nodes.html",{"final_data":final_data})

# To load data without refreshing


def load_table(request): 
	final_data=get_final_data()

	return render(request,"load_table.html",{"final_data":final_data})	
	
	
	
	