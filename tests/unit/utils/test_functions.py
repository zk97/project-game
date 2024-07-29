import unittest
import src.utils.functions as functions

class TestFunctions(unittest.TestCase):
    
    def test_slow_print(self):
        return self.assertIsNone(functions.slow_print("Pregunta"))


if __name__ == '__main__':
    unittest.main()