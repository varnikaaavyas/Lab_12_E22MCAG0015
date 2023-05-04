import dough
class Pizza:

    def __init__(self, cost, dough, cheese, sauce) -> None:
        self.__cost = cost
        self.__dough = dough
        self.__cheese = cheese
        self.__sauce = sauce

    def calculate_cost(self):
        return self.__cost + self.__dough.get_cost() + self.__cheese.get_cost() + self.__sauce.get_cost()
    
    def print_details(self):
        print('--- details---\n')
        print('-----------------------------------')
        print('|', self.__class__.__name__, '|', self.__cost, '|')
        print('|', self.__dough.__class__.__name__, '|', self.__dough.get_cost(), '|')
        print('|', self.__cheese.__class__.__name__, '|', self.__cheese.get_cost(), '|')
        print('|', self.__sauce.__class__.__name__, '|', self.__sauce.get_cost(), '|')
        print('------------------------------------')
        print('|', 'Total: \t', '|', self.calculate_cost(), '|')
        

    
