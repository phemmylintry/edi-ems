from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    EmployeeViewSet,
    TeamEmployeeViewSet,
    TeamLeaderViewSet,
    TeamViewSet,
    WorkArrangementViewSet,
)

router = DefaultRouter()

router.register(r"employees", EmployeeViewSet, basename="employees")
router.register(r"teams", TeamViewSet, basename="teams")
router.register(r"team-employees", TeamEmployeeViewSet, basename="team-employees")
router.register(r"team-leaders", TeamLeaderViewSet, basename="team-leaders")
router.register(
    r"work-arrangements", WorkArrangementViewSet, basename="work-arrangements"
)

urlpatterns = [] + router.urls
