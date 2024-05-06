from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
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
    r"assign-tasks", AssignDetailsViewSet,
    basename="assign-details"
)

# Global Routes

urlpatterns = [
    # Admin Route
    path('admin/', admin.site.urls),

    # JWT Routes
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # App Route
    path('api/v1/', include(router.urls)),
]
