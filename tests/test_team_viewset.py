import pytest
from api.models import Team
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestTeamViewSet:
    def test_list_team(self, api_client, test_team_1, test_team_2):
        url = reverse("teams-list")
        response = api_client.get(url)

        data = response.data

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(data, list)
        assert len(data) == 2
        assert data[0]["name"] == test_team_1.name
        assert data[1]["name"] == test_team_2.name

    def test_create_team(self, api_client):
        url = reverse("teams-list")
        data = {"name": "Team 3"}
        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert Team.objects.count() == 1

    def test_retrieve_team(self, api_client, test_team_1):
        url = reverse("teams-detail", kwargs={"pk": test_team_1.pk})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == test_team_1.name

    def test_update_team(self, api_client, test_team_1):
        url = reverse("teams-detail", kwargs={"pk": test_team_1.pk})
        data = {"name": "Team 3"}
        response = api_client.put(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == data["name"]

    def test_delete_team(self, api_client, test_team_1):
        url = reverse("teams-detail", kwargs={"pk": test_team_1.pk})
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Team.objects.count() == 0
