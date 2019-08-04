from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from myapp import views

urlpatterns = [
path('table/',views.table,name='table'),
path('adduser',views.adduser,name='adduser'),
path('deleteuser',views.deleteuser,name='deleteuser'),
path('success',views.success,name='success'),
path('delete',views.delete,name='delete'),
path('chart',views.chart,name='chart'),
path('load_chart.html',views.load_chart,name='load_chart'),
path('load_nodes.html',views.load_nodes,name='load_nodes'),
path('table/load_table.html',views.load_table,name='load_table'),
url(r'^$',views.hello,name='hello'),

]