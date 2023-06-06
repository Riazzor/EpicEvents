from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register('customer', views.CustomerViewSet)
router.register('contract', views.ContractViewSet)
router.register('event', views.EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
