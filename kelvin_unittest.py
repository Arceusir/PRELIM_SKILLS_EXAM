from Temperature1 import Temperature
import unittest

print(Temperature)

class Kelvin_Test(unittest.TestCase):
    def test_celsius(self):
        self.assertEqual(Temperature(celsius=10).kelvin,283.15)

    def test_fahrenheit(self):
        self.assertEqual(Temperature(fahrenheit=10).kelvin,264.8166666666667)

    def test_kelvin(self):
        self.assertEqual(Temperature(kelvin=10).kelvin,10)

    def test_NoArg(self):
        self.assertEqual(Temperature(kelvin=-1).kelvin,-1)

if __name__ == '__main__':
    unittest.main()

