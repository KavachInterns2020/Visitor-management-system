from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),

    path('host/',views.host,name='host'),
    path('host/<str:pk>',views.hostdynamic,name='hostdynamic'),
    path('create_host/',views.createhost,name='createhost'),
    path('update_host/<str:pk>',views.updateHost,name='updatehost'),
    path('delete_host/<str:pk>',views.deleteHost,name='deletehost'),


    path('visitor/',views.visitor,name='visitor'),
    path('create_visitor/',views.createvisitor,name='createvisitor'),
    path('update_visitor/<str:pk>',views.updatevisitor,name='updatevisitor'),
    path('delete_visitor/<str:pk>',views.deletevisitor,name='deletevisitor'),


    path('visitentry/',views.visitdetails,name='visitdetails'),

    path('eventvisitor/',views.eventvisitor,name='eventvisitor'),
    path('events/',views.events,name= 'events'),
]