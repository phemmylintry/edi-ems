import pytest
from api.models import Employee
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestEmployeeViewSet:
    def test_list_employee(self, api_client, test_employee_1, test_employee_2):
        url = reverse("employees-list")
        response = api_client.get(url)

        data = response.data

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(data, list)
        assert len(data) == 2
        assert data[0]["name"] == test_employee_1.name
        assert data[1]["name"] == test_employee_2.name

    def test_create_employee(self, api_client, test_team_1):
        url = reverse("employees-list")
        data = {"name": "Employee 3", "team": test_team_1.pk}
        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert Employee.objects.count() == 1

    def test_create_employee_with_invalid_team(self, api_client):
        url = reverse("employees-list")
        data = {"name": "Employee 3", "team": 1}
        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Employee.objects.count() == 0

    def test_create_employee_with_no_name(self, api_client, test_team_1):
        url = reverse("employees-list")
        data = {"team": test_team_1.pk}
        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Employee.objects.count() == 0

    def test_retrieve_employee(self, api_client, test_employee_1):
        url = reverse("employees-detail", kwargs={"pk": test_employee_1.pk})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == test_employee_1.name

    def test_update_employee(self, api_client, test_employee_1):
        url = reverse("employees-detail", kwargs={"pk": test_employee_1.pk})
        data = {"name": "Employee 3"}
        response = api_client.put(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == data["name"]

    def test_delete_employee(self, api_client, test_employee_1):
        url = reverse("employees-detail", kwargs={"pk": test_employee_1.pk})
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Employee.objects.count() == 0
