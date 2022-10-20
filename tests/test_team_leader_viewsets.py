import pytest
from api.models import TeamLeader
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestTeamLeaderViewSet:
    def test_list_team_leader(self, api_client, test_team_leader_1, test_team_leader_2):
        url = reverse("team-leaders-list")
        response = api_client.get(url)

        data = response.data
        print(data)
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(data, list)
        assert len(data) == 2
        assert data[0]["employee"] == test_team_leader_1.employee.pk
        assert data[1]["employee"] == test_team_leader_2.employee.pk

    def test_create_team_leader(self, api_client, test_employee_1, test_team_1):
        url = reverse("team-leaders-list")
        data = {"employee": test_employee_1.pk, "team": test_team_1.pk}
        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert TeamLeader.objects.count() == 1

    def test_retrieve_team_leader(self, api_client, test_team_leader_1):
        url = reverse("team-leaders-detail", kwargs={"pk": test_team_leader_1.pk})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["employee"] == test_team_leader_1.employee.pk

    def test_update_team_leader(self, api_client, test_team_leader_1, test_employee_2):
        url = reverse("team-leaders-detail", kwargs={"pk": test_team_leader_1.pk})
        data = {"employee": test_employee_2.pk, "team": test_team_leader_1.team.pk}
        response = api_client.put(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["employee"] == data["employee"]

    def test_delete_team_leader(self, api_client, test_team_leader_1):
        url = reverse("team-leaders-detail", kwargs={"pk": test_team_leader_1.pk})
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert TeamLeader.objects.count() == 0
