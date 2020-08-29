from itertools import count

from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from people.models import Neighbor
from people.serializers import NeighborSerializer, RadiusSearchSerializer
from rest_framework.test import APITestCase, APIClient


class GetAllNeighborsTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('people.urls'))
    ]

    @classmethod
    def setUpTestData(self):
        self.client = APIClient()
        # Create 13 neighbors for pagination tests
        self.number_of_neighbor = 13
        for neighbor_num in range(self.number_of_neighbor):
            Neighbor.objects.create(
                x_coord=0.32 + neighbor_num,
                y_coord=0.32 + neighbor_num,
                name=f'Sara {neighbor_num}'
            )

    def test_view_url_exists_at_desired_location(self):
        url = '/api/people/'
        response1 = self.client.get(url, format='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response1.data), 1)

    def test_get_all(self):
        neighbors = Neighbor.objects.all()
        serializer = NeighborSerializer(neighbors, many=True)
        self.assertEqual(len(serializer.data), self.number_of_neighbor)

    def test_get_valid_single_neighbor(self):
        response1 = self.client.get('/api/people/?pk=1', format='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        response2 = self.client.get('/api/people/?id=3/search', format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)






