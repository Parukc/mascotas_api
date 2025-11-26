from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clinic import views

router = routers.DefaultRouter()
router.register(r'mascotas', views.MascotaViewSet, basename='mascota')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/mascotas/control-peso', views.control_peso, name='control-peso'),
    path('api/tratamientos/dosis-total', views.dosis_total, name='dosis-total'),
]
