from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from register_app import views
from first_app import views
from django.views import generic

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^users/',include('register_app.urls')),
    url(r'^reviews/',include('first_app.urls')),
    url(r'^admin/', admin.site.urls),

]
