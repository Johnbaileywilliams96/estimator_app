# /backendproject/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backendapi.views import ClientViewSet
from backendapi.views import LibraryViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'libraries', LibraryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('backendapi.urls')),  
]

