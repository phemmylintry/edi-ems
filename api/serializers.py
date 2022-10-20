from unicodedata import decimal
from rest_framework import serializers
from .utils import calculate_employee_monthly_salary

from .models import Employee, Team, TeamEmployee, TeamLeader, WorkArrangement


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamEmployee
        fields = "__all__"


class TeamLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamLeader
        fields = "__all__"


class WorkArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkArrangement
        fields = "__all__"


class EmployeesSalarySerializer(serializers.ModelSerializer):
    salary = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ["name", "employee_id", "salary"]

    def get_salary(self, obj) -> float:
        hourly_rate = float(obj.hourly_rate)
        hours_per_week = obj.work_arrangements.hours_per_week

        # check if employee is team leader of any team using reverse relation
        try:
            team_leader = obj.team_leader_employee
        except TeamLeader.DoesNotExist:
            team_leader = None

        return calculate_employee_monthly_salary(
            hourly_rate, hours_per_week, team_leader
        )
