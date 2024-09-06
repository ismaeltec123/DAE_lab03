from django.urls import path
from . import views
app_name='candidatos'

urlpatterns=[
    path('',views.index,name='index'),

]