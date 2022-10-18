from rest_framework.viewsets import ModelViewSet

from .models import Employee, Team, TeamEmployee, TeamLeader, WorkArrangement
from .serializers import (
    EmployeeSerializer,
    TeamEmployeeSerializer,
    TeamLeaderSerializer,
    TeamSerializer,
    WorkArrangementSerializer,
)


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamEmployeeViewSet(ModelViewSet):
    queryset = TeamEmployee.objects.all()
    serializer_class = TeamEmployeeSerializer


class TeamLeaderViewSet(ModelViewSet):
    queryset = TeamLeader.objects.all()
    serializer_class = TeamLeaderSerializer


class WorkArrangementViewSet(ModelViewSet):
    queryset = WorkArrangement.objects.all()
    serializer_class = WorkArrangementSerializer
