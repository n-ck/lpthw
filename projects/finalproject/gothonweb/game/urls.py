from django.conf.urls import url

from . import views

app_name = 'game'

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^centralcorridor/$', views.CentralCorridor.as_view(), name='room'),
    url(r'^laserweaponarmory/$', views.LaserWeaponArmory.as_view(), name='room')
]