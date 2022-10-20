import pytest
from api.models import TeamEmployee
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestTeamEmployeeViewSet:
    def test_list_team_employee(self, api_client, test_employee_1, test_employee_2):
        url = reverse("team-employees-list")
        response = api_client.get(url)

        data = response.data

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(data, list)
        assert len(data) == 2
        assert data[0]["employee"] == test_employee_1.pk
        assert data[1]["employee"] == test_employee_2.pk

    def test_create_team_employee(self, api_client, test_team_2, test_employee_1):
        url = reverse("team-employees-list")
        data = {"team": test_team_2.pk, "employee": test_employee_1.pk}
        response = api_client.post(url, data=data)

        data = response.data

        # will fail because of the unique constraint, each employee can only be in one team
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert isinstance(data, dict)

    def test_retrieve_team_employee(self, api_client, test_team_1, test_employee_1):
        url = reverse("team-employees-detail", args=[test_team_1.pk])
        response = api_client.get(url)

        data = response.data

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(data, dict)
        assert data["employee"] == test_employee_1.pk

    def test_update_team_employee(self, api_client, test_team_1, test_employee_1):
        url = reverse("team-employees-detail", args=[test_team_1.pk])
        data = {"team": test_team_1.pk, "employee": test_employee_1.pk}
        response = api_client.put(url, data=data)

        data = response.data

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(data, dict)
        assert data["employee"] == test_employee_1.pk

    def test_delete_team_employee(self, api_client, test_team_1, test_employee_1):
        url = reverse("team-employees-detail", args=[test_team_1.pk])
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert (
            TeamEmployee.objects.filter(
                team=test_team_1.pk, employee=test_employee_1.pk
            ).count()
            == 0
        )
