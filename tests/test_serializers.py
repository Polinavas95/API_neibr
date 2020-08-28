from decimal import Decimal
from itertools import count

from django.test import TestCase
from django.urls import reverse

from people.models import Neighbor
from people.serializers import NeighborSerializer, RadiusSearchSerializer


class RadiusSearchSerializerTestClass(TestCase):

    @classmethod
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.neighbor_data= {
            'x_coord': Decimal('23.45'),
            'y_coord': Decimal('10.35'),
            'name': 'Bob'
        }
        self.serializer_1 = {
            'x_coord': Decimal('23.45'),
            'y_coord': Decimal('10.35'),
            'name': 'Bob',
            'id': 1
        }
        self.serializer_2 = {
            'x_coord': Decimal('23.45'),
            'y_coord': Decimal('10.35'),
            'name': 'Bob',
            'distance': Decimal('30.41')
        }
        self.neighbor = Neighbor.objects.create(**self.neighbor_data)
        self.serializer1 = NeighborSerializer(instance=self.serializer_1)
        self.serializer2 = RadiusSearchSerializer(instance=self.serializer_2)

    def test_contains_expected_fields(self):
        data1 = self.serializer1.data
        self.assertEqual(data1.keys(), set(['x_coord', 'y_coord', 'name', 'id']))
        data2 = self.serializer2.data
        self.assertEqual(data2.keys(), set(['x_coord', 'y_coord', 'name', 'distance']))

    def test_fields_content(self):
        data1 = self.serializer1.data
        self.assertEqual(data1['x_coord'], float(self.neighbor_data['x_coord']))
        self.assertEqual(data1['y_coord'], float(self.neighbor_data['y_coord']))
        self.assertEqual(data1['name'], self.neighbor_data['name'])
        data2 = self.serializer2.data
        self.assertEqual(data2['x_coord'], self.neighbor_data['x_coord'])
        self.assertEqual(data2['y_coord'], self.neighbor_data['y_coord'])
        self.assertEqual(data2['name'], self.neighbor_data['name'])

    def test_size_lower_bound_x(self):
        self.serializer_1['x_coord'] = 29.9
        self.serializer_1['y_coord'] = 29.9
        serializer = NeighborSerializer(data=self.serializer_1)
        self.assertTrue(serializer.is_valid())
        self.assertNotEqual(set(serializer.errors), set(['x_coord']))
        self.assertNotEqual(set(serializer.errors), set(['y_coord']))
        self.serializer_2['x_coord'] = 29.9
        self.serializer_2['y_coord'] = 29.9
        self.serializer_2['distance'] = 29.9
        serializer = RadiusSearchSerializer(data=self.serializer_2)
        self.assertTrue(serializer.is_valid())
        self.assertNotEqual(set(serializer.errors), set(['x_coord']))
        self.assertNotEqual(set(serializer.errors), set(['y_coord']))
        self.assertNotEqual(set(serializer.errors), set(['distance']))

    def test_size_upper_bound_x(self):
        self.serializer_1['x_coord'] = 60.1
        self.serializer_1['x_coord'] = 60.1
        serializer = NeighborSerializer(data=self.serializer_1)
        self.assertTrue(serializer.is_valid())
        self.assertNotEqual(set(serializer.errors), set(['x_coord']))
        self.assertNotEqual(set(serializer.errors), set(['y_coord']))
        self.serializer_2['x_coord'] = 60.1
        self.serializer_2['x_coord'] = 60.1
        self.serializer_2['distance'] = 60.1
        serializer = RadiusSearchSerializer(data=self.serializer_2)
        self.assertTrue(serializer.is_valid())
        self.assertNotEqual(set(serializer.errors), set(['x_coord']))
        self.assertNotEqual(set(serializer.errors), set(['y_coord']))
        self.assertNotEqual(set(serializer.errors), set(['distance']))

    def test_coord_must_be_in_choices(self):
        self.neighbor_data['x_coord'] = 2.34
        self.neighbor_data['y_coord'] = 2.34
        self.neighbor_data['name'] = 'name'
        serializer = NeighborSerializer(instance=self.neighbor, data=self.neighbor_data)
        self.assertFalse(serializer.is_valid())
        self.assertNotEqual(set(serializer.errors.keys()), set(['x_coord']))
        self.assertNotEqual(set(serializer.errors.keys()), set(['y_coord']))
        self.assertNotEqual(set(serializer.errors.keys()), set(['name']))
        serializer = RadiusSearchSerializer(instance=self.neighbor, data=self.neighbor_data)
        self.assertFalse(serializer.is_valid())
        self.assertNotEqual(set(serializer.errors.keys()), set(['x_coord']))
        self.assertNotEqual(set(serializer.errors.keys()), set(['y_coord']))
        self.assertNotEqual(set(serializer.errors.keys()), set(['name']))









