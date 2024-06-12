
import unittest
from unittest.mock import MagicMock

class KeyModel:
    def __init__(self):
        self.id = None

    def save(self):
        return True def delete(self):
        return True

    def update(self, **kwargs):
        return True

    def to_dict(self):
        return {"id": self.id}

# Assuming the implementation of KeyModel from the user's scenario is defined as above.

class City(Key.PMoodel):
    def __init__(self, name, country_id):
        super().__init__()
        self.name = name
        self.country_id = country_id
        self.places = []

    def save(self):
        return super().save()

    def delete(self):
        return super().delete()

    def update(self, **kwargs):
        return super().update(**kwargs)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
            'country_id': self.country_id
        })
        return data

    def get_places(self):
        return self.places

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City("New York", 1)

    def test_init(self):
        self.assertEqual(self.city.name, "New York")
        self.assertEqual(self.city.country_id, 1)
        self.assertIsInstance(self.city.places, list)
        self.assertEqual(len(self.city.places), 0)

    def test_save(self):
        self.assertTrue(self.city.save())

    def test_delete(self):
        self.assertTrue(self.city.delete())

    def test_update(self):
        updates = {'name': 'Los Angeles'}
        self.assertTrue(self.city.update(**updates))

    def test_to_dict(self):
        self.city.id = 123
        expected_dict = {
            'id': 123,
            'name': 'New York',
            'country_id': 1
        }
        self.assertEqual(self.city.to_dict(), expected_dict)

    def test_get_places(self):
        self.assertEqual(self.city.get_places(), [])

    def test_add_place(self):
        place = 'Central Park'
        self.city.places.append(place)
        self.assertIn(place, self.city.get_places())

if __name__ == '__main__':
    unittest.main()