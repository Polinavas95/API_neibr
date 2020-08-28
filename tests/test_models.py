from django.test import TestCase

from people.models import Neighbor


class ModelsTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Neighbor.objects.create(x_coord=23.45, y_coord=10.34, name='Bob')

    def test_name_label(self):
        neighbor = Neighbor.objects.get(id=1)
        field_label = neighbor._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        neighbor = Neighbor.objects.get(id=1)
        max_length = neighbor._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_x_coord_maximum_digits(self):
        neighbor = Neighbor.objects.get(id=1)
        max_digits = neighbor._meta.get_field('x_coord').max_digits
        self.assertEquals(max_digits, 5)

    def test_x_coord_decimal_places(self):
        neighbor = Neighbor.objects.get(id=1)
        decimal_places = neighbor._meta.get_field('x_coord').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_y_coord_maximum_digits(self):
        neighbor = Neighbor.objects.get(id=1)
        max_digits = neighbor._meta.get_field('y_coord').max_digits
        self.assertEquals(max_digits, 5)

    def test_y_coord_decimal_places(self):
        neighbor = Neighbor.objects.get(id=1)
        decimal_places = neighbor._meta.get_field('y_coord').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_object_name_is_name(self):
        neighbor = Neighbor.objects.get(id=1)
        expected_object_name = neighbor.name
        self.assertEquals(expected_object_name, str(neighbor))