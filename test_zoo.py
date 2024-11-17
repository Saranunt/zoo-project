import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(25), 150)

    def test_elderly_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(75), 100)
       
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()