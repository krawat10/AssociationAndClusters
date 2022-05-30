import numpy as np
from utils import powerset


class Transaction:
    products: []

    def items_number(self) -> int:
        return len(self.products)

    def __init__(self, products):
        self.products = products

    def contain(self, products) -> bool:
        if len(products) > len(self.products):
            return False

        for product in products:
            if product not in self.products:
                return False

        return True

    def get_combinations(self, size: int):
        return list(powerset(self.products, size))
