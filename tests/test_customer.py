import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(1, "John", "Doe", "John@doe.com", "1234567890", "123 Main St", "1997-06-13")

    # Test if a customer object is created correctly
    def test_create_customer(self):
        
        self.assertEqual(self.customer.Customer_ID, 1)
        self.assertEqual(self.customer.FName, "John")
        self.assertEqual(self.customer.LName, "Doe")
        self.assertEqual(self.customer.Email, "John@doe.com")
        self.assertEqual(self.customer.Phone, "1234567890")
        self.assertEqual(self.customer.Address, "123 Main St")
        self.assertEqual(self.customer.Date_Of_Birth, "1997-06-13")

    # Test if the display_info method returns expected output
    def test_display_info(self):

        info = self.customer.display_info()
        self.assertIn("Customer ID: 1", info)
        self.assertIn("Name: John Doe", info)
        self.assertIn("Email: John@doe.com", info)
        self.assertIn("Phone: 1234567890", info)

if __name__ == '__main__':
    unittest.main()
