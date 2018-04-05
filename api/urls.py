from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'person/$', views.PersonListAPI.as_view()),
    url(r'job_detail/$', views.JobDetailListAPI.as_view()),
    url(r'automotive/$', views.AutomotiveListAPI.as_view()),
]