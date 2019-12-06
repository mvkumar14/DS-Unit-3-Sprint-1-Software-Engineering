from random import randint


class Product():
    """ Base class for all acme products """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """ Function that returns the stealability of a given acme products.
        The function outputs one of three very precise responses that determine
        the stealability of your product.

        (Remember all purchases are final, and acme is not liabale for
        theft of your products)"""
        ratio = self.price/self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio < 1:
            return "Kinda stealable"
        else:
            return "Very stealable"

    def explode(self):
        """Function that returns the magnitude of the explosion when an acme
        product is ... exploded

        All explosions, including accidental explsions of acme products are
        the sole responsibility of the buyer.

        Praise for acme products:
        "This thing blew me away."
        "I can see why the coyote hasn't ever caught the roadrunner"
        "WHY DID YOU MAKE THE EXPLODE BUTTON SO DAMN BIG!"

                                    - our valued customers
        """
        boom_factor = self.flammability*self.weight
        if boom_factor < 10:
            return "... fizzle"
        elif boom_factor >= 10:
            return "... boom"
        else:
            return "... BABOOM!!"
        pass


class BoxingGlove(Product):
    """Subclass for the acme boxing glove (inherits from Product class)"""
    def __init__(self, name, weight=10):
        # This attribute override isn't the same as what we did in class.
        # There may be unintended consequences to this that I do not know of.
        super().__init__(name, weight=weight)

    def explode(self):
        """ What happens when you explode the boxing glove """
        return ("... it\'s a glove... there wasn\'t even a button... " +
        "how did you even get here?")

    def punch(self):
        """ User response when punched by the glove """
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
