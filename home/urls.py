from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.contactdisplay,name='contactdisplay'),
    path('savecontact/',views.savecontact,name='savecontact'),
    path('contactdisplay/',views.contactdisplay,name='contactdisplay'),
    path('delete/<int:id>',views.deletecontact,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('formUpdate/<int:id>',views.formUpdate,name='formUpdate'),
    path('search',views.search,name='search')
]