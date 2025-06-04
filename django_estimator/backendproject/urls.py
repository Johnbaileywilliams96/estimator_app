# /backendproject/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backendapi.views import ClientViewSet
from backendapi.views import LibraryViewSet
from backendapi.views import SublibraryViewSet
from backendapi.views import ItemServicesViewSet
from backendapi.views import BusinessViewSet



router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'libraries', LibraryViewSet)
router.register(r'sublibraries', SublibraryViewSet)
router.register(r'itemservices', ItemServicesViewSet)
router.register(r'business', BusinessViewSet, "business")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('backendapi.urls')),  
]
