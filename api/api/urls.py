from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import PostViewSet
from core import views

router = DefaultRouter()

router.register(r"posts", views.PostViewSet, basename = 'post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls), name='api')
]
