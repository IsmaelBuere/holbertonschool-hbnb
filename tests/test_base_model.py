#!/usr/bin/python3

import unittest, uuid, time
from models.base_model import KeyModel
from datetime import datetime


# Esta es una clase de prueba que hereda de KeyModel.
# La usamos para probar las funcionalidades de KeyModel.
class TestKeyModel(KeyModel):
    def __init__(self):
        super().__init__()
        self.name = "Test"  # Un atributo adicional para pruebas

    def save(self):
        # Simulamos la acción de guardar actualizando updated_at al tiempo actual
        self.updated_at = datetime.now()

    def delete(self):
        # Simulamos la acción de eliminar. Aquí no hacemos nada concreto.
        pass

# Clase de pruebas unitarias para KeyModel.
# unittest.TestCase es la clase base para crear nuevas pruebas unitarias.
class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Este método se llama antes de cada prueba.
        # Aquí creamos una nueva instancia de TestKeyModel para cada prueba.
        self.instance = TestKeyModel()

    def test_initialization(self):
        # Esta prueba verifica que la instancia se inicialice correctamente.
        self.assertIsNotNone(self.instance.id)  # Verificamos que el id no sea None
        self.assertIsInstance(self.instance.id, uuid.UUID)  # Verificamos que el id sea de tipo UUID
        self.assertIsInstance(self.instance.created_at, datetime)  # Verificamos que created_at sea un datetime
        self.assertIsInstance(self.instance.updated_at, datetime)  # Verificamos que updated_at sea un datetime
        self.assertEqual(self.instance.name, "Test")  # Verificamos que el atributo name sea "Test"

    def test_update(self):
        # Esta prueba verifica que el método update funcione correctamente.
        old_updated_at = self.instance.updated_at  # Guardamos el valor antiguo de updated_at
        time.sleep(0.001)  # Esperamos un poco para asegurar que el tiempo cambie
        self.instance.update(name="Updated Test")  # Actualizamos el atributo name
        self.assertEqual(self.instance.name, "Updated Test")  # Verificamos que name se haya actualizado
        self.assertNotEqual(self.instance.updated_at, old_updated_at)  # Verificamos que updated_at haya cambiado

    def test_to_dict(self):
        # Esta prueba verifica que el método to_dict funcione correctamente.
        data = self.instance.to_dict()  # Convertimos la instancia a un diccionario
        self.assertEqual(data['id'], self.instance.id)  # Verificamos que el id en el diccionario sea correcto
        self.assertEqual(data['created_at'], self.instance.created_at)  # Verificamos que created_at sea correcto
        self.assertEqual(data['updated_at'], self.instance.updated_at)  # Verificamos que updated_at sea correcto
        self.assertIn('id', data)  # Verificamos que 'id' esté en el diccionario
        self.assertIn('created_at', data)  # Verificamos que 'created_at' esté en el diccionario
        self.assertIn('updated_at', data)  # Verificamos que 'updated_at' esté en el diccionario

# Esta línea permite ejecutar las pruebas desde la línea de comandos.
if __name__ == '__main__':
    unittest.main()
