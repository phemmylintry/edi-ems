import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestWorkArrangementViewSet:
    def test_list_work_arrangement(self, api_client, test_employee_1, test_employee_2):
        url = reverse("work-arrangements-list")
        response = api_client.get(url)

        data = response.data
        print(data)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(data, list)
        assert len(data) == 2
        assert data[0]["employee"] == test_employee_1.pk
        assert data[1]["employee"] == test_employee_2.pk
