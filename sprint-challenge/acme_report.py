from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def avg(list):
    """Function to calculate the average value of a list of numerical values"""
    return sum(list)/len(list)


def generate_products(num_products=30):
    """ Function to randomly generate a list of n products where n is the
    parameter passed to the function"""
    products = []
    for i in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + " " + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products.append(Product(name, price, weight, flammability))
    return products


def inventory_report(products):
    """ Function to report information on a list of products. Report includes:
    number of unique products, average price, average weight, and average,
    flammability of the products in the list"""

    # Extract lists of information from the object list:
    names, prices, weights, flams = [prod.name, prod.price, prod.weight,
        prod.flammability for prod in products]

    # The following two lines test that names is written correctly.
    # print(len(set(names)),len(names))
    # print(names)

    # Number of unique names:
    num_prod_names = len(set(names))

    # Average price:
    avg_price = avg(prices)

    # Average weight:
    avg_weight = avg(weights)

    # Average flammability
    avg_flam = avg(flams)

    # Print out the information in a neat way.
    print(f"ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f"Unique product names: {num_prod_names}")
    print(f"Average price: ${avg_price:,.02f}")
    print(f"Average weight: {avg_weight:.02f}")
    print(f"Average flammability: {avg_flam:.02f}")


if __name__ == '__main__':
    # Used the following to test the generate_products code:
    # print(generate_products()[0].name)
    inventory_report(generate_products())
