import unittest

from src.exceptions import NumeroDebeSerPositivo
from src.exceptions import ingrese_numero
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        """Test para verificar que se acepte un número positivo correctamente."""
        numero = ingrese_numero()
        self.assertEqual(numero, 100)
    
    @patch('builtins.input', return_value='0')
    def test_ingreso_cero(self, patch_input):
        """Test para verificar que se acepte el cero como número válido."""
        numero = ingrese_numero()
        self.assertEqual(numero, 0)
    
    @patch('builtins.input', return_value='1')
    def test_ingreso_uno(self, patch_input):
        """Test para verificar que se acepte 1 como número válido."""
        numero = ingrese_numero()
        self.assertEqual(numero, 1)
    
    @patch('builtins.input', return_value='999999')
    def test_ingreso_numero_grande(self, patch_input):
        """Test para verificar que se acepten números grandes."""
        numero = ingrese_numero()
        self.assertEqual(numero, 999999)

    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        """Test para verificar que se rechace un número negativo."""
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
    
    @patch('builtins.input', return_value='-1')
    def test_ingreso_negativo_uno(self, patch_input):
        """Test para verificar que se rechace -1 como número negativo."""
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
    
    @patch('builtins.input', return_value='-999999')
    def test_ingreso_negativo_grande(self, patch_input):
        """Test para verificar que se rechacen números negativos grandes."""
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
            
    @patch('builtins.input', return_value='AAA')
    def test_ingreso_letras(self, patch_input):
        """Test para verificar que se rechacen entradas de texto."""
        with self.assertRaises(ValueError):
            ingrese_numero()
    
    @patch('builtins.input', return_value='')
    def test_ingreso_vacio(self, patch_input):
        """Test para verificar que se rechacen entradas vacías."""
        with self.assertRaises(ValueError):
            ingrese_numero()
    
    @patch('builtins.input', return_value='12.34')
    def test_ingreso_decimal(self, patch_input):
        """Test para verificar que se rechacen números decimales (como texto con punto)."""
        with self.assertRaises(ValueError):
            ingrese_numero()
                    
if __name__ == '__main__':
    unittest.main()