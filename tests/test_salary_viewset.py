import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestSalaryViewSet:
    def test_list_salary(self, api_client, test_employee_1, test_employee_2):
        url = reverse("list-employees-salary-list")
        response = api_client.get(url)

        data = response.data

        print(data)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(data, list)
        assert len(data) == 2
        assert "salary" in data[0] and "salary" in data[1]
