from random import randint


class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price/self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio < 1:
            return "Kinda stealable"
        else:
            return "Very stealable"

    def explode(self):
        boom_factor = self.flammability*self.weight
        if boom_factor < 10:
            return "... fizzle"
        elif boom_factor >= 10:
            return "... boom"
        else:
            return "... BABOOM!!"
        pass


class BoxingGlove(Product):
    def __init__(self, weight=10):
        # This attribute override isn't the same as what we did in class.
        # There may be unintended consequences to this that I do not know of.
        self.weight = weight

    def explode(self):
        return "... it's a glove"

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
