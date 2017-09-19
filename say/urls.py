from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^testpost/$',views.testpost),
    url(r'^json1/$',views.json1),
    url(r'^json2/$', views.json2),

]