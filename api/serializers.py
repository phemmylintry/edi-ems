from unicodedata import decimal
from rest_framework import serializers
from .utils import calculate_employee_monthly_salary

from .models import Employee, Team, TeamEmployee, TeamLeader, WorkArrangement


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ("created_at", "updated_at")


class EmployeeSerializer(serializers.ModelSerializer):
    # team = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        exclude = ("created_at", "updated_at")

    # def get_team(self, obj):
    #     return TeamSerializer(obj.team).data


class TeamEmployeeSerializer(serializers.ModelSerializer):
    # employee = serializers.SerializerMethodField()
    # team = serializers.SerializerMethodField()

    class Meta:
        model = TeamEmployee
        exclude = ("created_at", "updated_at")

    # def get_employee(self, obj):
    #     return EmployeeSerializer(obj.employee).data

    # def get_team(self, obj):
    #     return TeamSerializer(obj.team).data


class TeamLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamLeader
        exclude = ("created_at", "updated_at")


class WorkArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkArrangement
        exclude = ("created_at", "updated_at")


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
