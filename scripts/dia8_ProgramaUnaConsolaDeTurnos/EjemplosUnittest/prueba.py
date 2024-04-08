import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):
    
    def test_mayusculas(self):
        palabra = 'buenos días'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUENOS DÍAS')
        
    def test_mayusculas_erroneo(self):
        palabra = 'buenos días'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertNotEqual(resultado, 'BuEnoS DíAs')
        
if __name__ == '__main__':
    unittest.main()