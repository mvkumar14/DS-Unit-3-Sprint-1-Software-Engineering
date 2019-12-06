import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price is 10"""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weigh(self):
        """Test that the default weight is 20"""
        prod = Product("Test Product")
        self.assertEqual(prod.weight, 20)

    def test_steal_explode_functions(self):
        """Test that stealability and explode functions are working as they
        should for the "lowest" values of each"""
        prod = Product("Test", 5, 11, 0.2)
        self.assertEqual(prod.stealability(), "Not so stealable...")
        self.assertEqual(prod.explode(), "... fizzle")


class AcmeReportTests(unittest.TestCase):
    """ Making sure that the reporting functions work properly"""
    def test_default_num_products(self):
        """Test that the object generator generates the proper number of
        products"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test that the names that are produced are legal"""
        # You can manually check failure condition output with the following:
        # self.assertIn("whoops",ADJECTIVES)
        # self.assertIn("nothere",NOUNS)
        prods = generate_products()
        for item in prods:
            name = item.name.split(" ")
            adj = name[0]
            noun = name[1]
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)


if __name__ == '__main__':
    unittest.main()
