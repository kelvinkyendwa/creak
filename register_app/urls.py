from django.conf.urls import url
from register_app import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
]
