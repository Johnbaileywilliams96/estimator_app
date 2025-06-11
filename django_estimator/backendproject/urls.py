# /backendproject/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backendapi.views import ClientViewSet
from backendapi.views import LibraryViewSet
from backendapi.views import SublibraryViewSet
from backendapi.views import ItemServicesViewSet
from backendapi.views import BusinessViewSet
from backendapi.views import ItemPricingViewSet
from backendapi.views import ProjectViewSet
from backendapi.views import UnitOfMeasureViewSet
from rest_framework.authtoken.views import obtain_auth_token
from backendapi.views import login_user, register_user, logout_user


router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'libraries', LibraryViewSet)
router.register(r'sublibraries', SublibraryViewSet)
router.register(r'itemservices', ItemServicesViewSet)
router.register(r'business', BusinessViewSet, "business")
router.register(r'pricing', ItemPricingViewSet, "pricing")
router.register(r'project', ProjectViewSet, "project")
router.register(r'unitofmeasure', UnitOfMeasureViewSet, "unitofmeasure")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', login_user, name='login'),
    path('auth/register/', register_user, name='register'),
    path('auth/logout/', logout_user, name='logout'),
    path('', include(router.urls)),
    path('api/', include('backendapi.urls')),  
]
