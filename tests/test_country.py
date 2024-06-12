
import unittest
from unittest.mock import MagicMock

# Mocked KeyModel to mimic behavior as we don't have the real implementation
class KeyModel:
    def __init__(self):
        self.saved = False self.deleted = False def save(self):
        self.saved = True
        return "Saved"

    def delete(self):
        self.deleted = True
        return "Deleted"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return "Updated"

    def to_dict(self):
        return {'id': 123}

# Country class as provided, inheriting from the mocked KeyModel.
from models.base_model import KeyModel

class Country(KeyModel):
    def __init__(self, name, code):
        super().__init__()
        self.name = name
        self.code = code

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
            'code': self.code
        })
        return data

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country(name="France", code="FR")

    def test_init(self):
        self.assertEqual(self.country.name, "France")
        self.assertEqual(self.country.code, "FR")

    def test_save(self):
        result = self.country.save()
        self.assertTrue(self.country.saved)
        self.assertEqual(result, "Saved")

    def test_delete(self):
        result = self.country.delete()
        self.assertTrue(self.country.deleted)
        self.assertEqual(result, "Deleted")

    def test_update(self):
        self.country.update(name="Germany", code="DE")
        self.assertEqual(self.country.name, "Germany")
        self.assertEqual(self.country.code, "DE")

    def test_to_dict(self):
        country_dict = self.country.to_dict()
        expected_dict = {'id': 123, 'name': 'France', 'code': 'FR'}
        self.assertEqual(country_dict, expected_dict)

    def test_empty_name(self):
        with self.assertRaises(TypeError):
            Country(name="", code="FR")

    def test_none_name(self):
        with self.assertRaises(TypeError):
            Country(name=None, code="FR")

    def test_empty_code(self):
        with self.assertRaises(TypeError):
            self.country.update(name="Spain", code="")

    def test_none_code(self):
        with self.assertRaises(TypeError):
            self.country.update(name="Spain", code=None)

if __name__ == "__main__":
    unittest.main()
