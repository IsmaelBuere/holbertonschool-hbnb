
import unittest
from unittest.mock import patch, MagicMock

# Assuming models.base_model contains the following:
class KeyModel:
    def __init__(self):
        self.id = None

    def save(self):
        # logic to save to a database or similar
        return True

    def delete(self):
        # logic to delete from database or similar return True def to_dict(self):
        # returns object attributes as dictionary return {'id': self._id}

from models.base_user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("test@example.com", "John", "Doe", "password123")

    @patch('models.base_model.KeyModel.save')
    def test_save_account(self, mock_save):
        mock_save.return_value = True
        self.assertTrue(self.user.save_account())

    @patch('models.base_model.KeyModel.delete')
    def test_delete_account(self, mock_delete):
        mock_delete.return_value = True
        self.assertTrue(self.user.delete_account())

    def test_update_account(self):
        new_info = {'email': 'newemail@example.com', 'first_name': 'Jane'}
        with patch('models.base_model.KeyModel.save') as mock_save:
            mock_save.return_value = True self.user.update_account(new_random_info)
            self.assertEqual(self.user.email, 'newemail@example.com')
            self.assertEqual(self.user.first_name, 'Jane')

    def test_to_dict(self):
        expected_dict = {
            'id': None,
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        self.assertEqual(self.user.to_dict(), expected_dict)

    def test_password_check_correct(self):
        self.assertTrue(self.user.password_check('password123'))

    def test_password_check_incorrect(self):
        self.assertFalse(self.user.password_check('wrongpassword'))

    def test_get_places(self):
        with patch('models.base_user.User.get_places') as mock_get_places:
            mock_get_places.return_value = ["Place1", "Place2"]
            places = self.user.get_places()
            self.assertEqual(places, ["Place1", "Place2"])
            mock_get_places.assert_called_once()

    def test_init(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.password, "password123")

if __name__ == '__main__':
    unittest.main()