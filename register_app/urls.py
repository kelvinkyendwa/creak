from django.conf.urls import url
from register_app import views

urlpatterns = [

    url(r'^$',views.help, name='help'),
    url(r'^register/',views.register, name='register'),
]
