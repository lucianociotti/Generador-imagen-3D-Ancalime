import unittest
from src import core_cad

class TestCoreCad(unittest.TestCase):
    def test_generate_cube(self):
        cube = core_cad.generate_cube(50)
        # Verificamos que se genera algún objeto (prueba simplificada)
        self.assertIsNotNone(cube)
    
    def test_export_to_stl(self):
        cube = core_cad.generate_cube(50)
        filename = "test_cube.stl"
        try:
            core_cad.export_to_stl(cube, filename)
            success = True
        except Exception as e:
            print("Error al exportar STL:", e)
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
