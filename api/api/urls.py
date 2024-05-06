from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import (
    UserViewSet,
    AuthorizationViewSet,
)
from task.views import (
    TaskViewSet,
    AssignDetailsViewSet
)

router = DefaultRouter()

 # User Routes!

router.register(
    r"users", UserViewSet, 
    basename='user'
)
router.register(
    r"authorization", 
    AuthorizationViewSet, 
    basename="authorization"
)

 # Task Routes!

router.register(
    r"tasks", TaskViewSet, 
    basename="tasks"
)

router.register(
    r"assign_tasks", AssignDetailsViewSet,
    basename="assign_details"
)

# Global Routes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
