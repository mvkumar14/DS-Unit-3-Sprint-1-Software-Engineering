from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def avg(list):
    return sum(list)/len(list)

def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        name = sample(ADJECTIVES,1)[0] + " " + sample(NOUNS,1)[0]
        price = randint(5,100)
        weight = randint(5,100)
        flammability = uniform(0,2.5)
        products.append(Product(name,price,weight,flammability))
    return products

def inventory_report(products):
    #Find out number of unique names:
    names = [prod.name for prod in products]
        # The following two lines test that names is written correctly.
        # print(len(set(names)),len(names))
        # print(names)
    num_prod_names = len(set(names))

    #Average price:
    prices = [prod.price for prod in products]
    avg_price = avg(prices)

    #Average weight:
    weights = [prod.weight for prod in products]
    avg_weight = avg(weights)

    #Average flammability
    flams = [prod.flammability for prod in products]
    avg_flam = avg(flams)

    print(f"ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f"Unique product names: {num_prod_names}")
    print(f"Average price: ${avg_price:,.02f}")
    print(f"Average weight: {avg_weight:.02f}")
    print(f"Average flammability: {avg_flam:.02f}")

if __name__ == '__main__':
    # Used the following to test the generate_products code:
    # print(generate_products()[0].name)
    inventory_report(generate_products())
