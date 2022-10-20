from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response


from .models import Employee, Team, TeamEmployee, TeamLeader, WorkArrangement
from .serializers import (
    EmployeeSerializer,
    TeamEmployeeSerializer,
    TeamLeaderSerializer,
    TeamSerializer,
    WorkArrangementSerializer,
    EmployeesSalarySerializer,
)


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.select_related("team").all()


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamEmployeeViewSet(ModelViewSet):
    serializer_class = TeamEmployeeSerializer

    def get_queryset(self):
        return TeamEmployee.objects.select_related("employee", "team").all()


class TeamLeaderViewSet(ModelViewSet):
    queryset = TeamLeader.objects.all()
    serializer_class = TeamLeaderSerializer


class WorkArrangementViewSet(ModelViewSet):
    queryset = WorkArrangement.objects.all()
    serializer_class = WorkArrangementSerializer


class EmployeesSalaryViewSet(ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSalarySerializer

    def get_queryset(self):
        # fetch related objects using reverse relation
        queryset = self.queryset.prefetch_related(
            "work_arrangements",
            "team_leader_employee",
        ).all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, 200)
