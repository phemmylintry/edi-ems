import pytest
from api.models import Employee, Team, TeamEmployee, TeamLeader, WorkArrangement
from rest_framework.test import APIClient


@pytest.fixture
def api_client(db):
    return APIClient()


@pytest.fixture
def test_team_1(db):
    return Team.objects.create(name="Team 1")


@pytest.fixture
def test_team_2(db):
    return Team.objects.create(name="Team 2")


@pytest.fixture
def test_employee_1(db, test_team_1):
    return Employee.objects.create(name="Employee 1", team=test_team_1, hourly_rate=25)


@pytest.fixture
def test_employee_2(db, test_team_2):
    return Employee.objects.create(name="Employee 2", team=test_team_2, hourly_rate=15)


@pytest.fixture
def test_team_leader_1(db, test_team_1, test_employee_1):
    return TeamLeader.objects.create(employee=test_employee_1, team=test_team_1)


@pytest.fixture
def test_team_leader_2(db, test_team_2, test_employee_2):
    return TeamLeader.objects.create(employee=test_employee_2, team=test_team_2)


@pytest.fixture
def test_team_employee_1(db, test_team_1, test_employee_1):
    return TeamEmployee.objects.create(employee=test_employee_1, team=test_team_1)


@pytest.fixture
def test_team_employee_2(db, test_team_2, test_employee_2):
    return TeamEmployee.objects.create(employee=test_employee_2, team=test_team_2)


@pytest.fixture
def test_work_arrangement_1(db, test_employee_1):
    return WorkArrangement.objects.create(
        employee=test_employee_1,
        work_arrangement=WorkArrangement.FULL_TIME,
        hours_per_week=40,
    )


@pytest.fixture
def test_work_arrangement_2(db, test_employee_2):
    return WorkArrangement.objects.create(
        employee=test_employee_2,
        work_arrangement=WorkArrangement.PART_TIME,
        hours_per_week=25,
    )
