import pizza

class Newyork_Style_Pizza(pizza.Pizza):
    
    def __init__(self, cost, dough, cheese, sauce) -> None:
        super().__init__(cost, dough, cheese, sauce)