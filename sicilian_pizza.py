import pizza

class Sicilian_Pizza(pizza.Pizza):
    
    def __init__(self, cost, dough, cheese, sauce) -> None:
        super().__init__(cost, dough, cheese, sauce)