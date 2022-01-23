from django.conf.urls import url
from Apps.Applicacion1 import views

urlpatterns=[
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),
]