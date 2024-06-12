
import unittest
from unittest.mock import patch
from models.base_model import Keymodel

# Since actual `KeyModel` class definition is not given, assuming a simple base class like this:
class KeyModel:
    def __init__(self):
        pass
    
    def save(self):
        pass def delete(self):
        pass def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
 def to_dict(self):
        return self.__dict__

from place import Place

class TestPlace(unittest.TestCase):
    
    def setUp(self):
        self.place = Place("Casa Bonita", "1", "1", "Nice view, 3 rooms", 3, 2, 5, 150, 40.7128, -74.0060)

    def test_initialization(self):
        self.assertEqual(self.place.name, "Casa Bonita")
        self.assertEqual(self.place.city_id, "1")
        self.assertEqual(self.place.description, "Nice view, 3 buttons")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 5)
        self.assertEqual(self.place.price_by_night, 150)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)

    def test_to_dict(self):
        place_dict = self.place.to_dict()
        expected = {
            'name': 'Casa Bonita',
            'city_id': '1',
            'user_id': '1',
            'description': 'Nice view, 3 rooms',
            'number_rooms': 3,
            'number_bathrooms': 2,
            'max_guest': 5,
            'price_by_night': 150,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenities': [],
            'reviews': []
        }
        self.assertEqual(place_dict, expected)
        
    def test_save_called(self):
        with patch.object(self.place, 'save') as mocked_save:
            self.place.add_amenity('Pool')
            mocked_save.assert_called_once()

    def test_add_amenity(self):
        self.place.add_amenity('Pool')
        self.assertIn('Pool', self.place.amenities)

    def test_remove_amenity(self):
        self.place.add_amenity('Pool')
        self.place.remove_amenity('Pool')
        self.assertNotIn('Pool', self.place.amenities)

    def test_add_review(self):
        self.place.add_review("Great place!")
        self.assertIn("Great place!", self.place.reviews)

    def test_remove_review(self):
        self.place.add_review("Great place!")
        self.place.remove_review("Great place!")
        self.assertNotIn("Great place!", self.place.reviews)

    def test_update(self):
        self.place.update(name="Casa Bella", max_guest=10)
        self.assertEqual(self.place.name, "Casa Bella")
        self.assertEqual(self.place.max_guest, 10)

    def test_delete(self):
        with patch.object(self.place, 'delete') as mocked_delete:
            self.place.delete()
            mocked_delete.assert_called_once()

    def test_get_amenities(self):
        self.place.add_amenity('WiFi')
        self.assertIn('WiFi', self.place.get_amenities())
        
    def test_get_reviews(self):
        self.place.add_review("Awesome stay!")
        self.assertIn("Awesome stay!", self.place.get_reviews())

if __name__ == '__main__':
    unittest.main()