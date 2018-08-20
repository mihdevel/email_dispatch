from rest_framework import routers
from rest_api import views

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'emails', views.EmailViewSet)
router.register(r'dispatchs', views.DispatchViewSet)