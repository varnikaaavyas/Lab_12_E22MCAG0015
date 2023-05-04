import barbecue_sauce, marinara_sauce, plum_tomato_sauce, pumpkin_sauce

import reggiano_cheese, provolone_cheese, mozzarella_cheese, parmesan_cheese

import thin_crust_dough, thick_crust_dough

import chicago_pizza, sicilian_pizza, newyork_style_pizza, greek_pizza

 

import os.path

import json

 

class Admin:

    def __init__(self):

        self.pizza_prices = {}

        self.sauce_prices = {}

        self.cheese_prices = {}

        self.dough_prices = {}

 

        if os.path.isfile('prices.json'):

            with open('prices.json', 'r') as f:

                prices = json.load(f)

                self.pizza_prices = prices['pizza_prices']

                self.sauce_prices = prices['sauce_prices']

                self.cheese_prices = prices['cheese_prices']

                self.dough_prices = prices['dough_prices']

        else:

            for pizza in ['Greek', 'Chicago', 'NewYork', 'Sicilian']:

                price = float(input(f"Enter the price for {pizza} pizza: "))

                self.pizza_prices[pizza] = price

               

            for sauce in ['PlumTomato', 'Marinara', 'Barbecue', 'Pumpkin']:

                price = float(input(f"Enter the price for {sauce} sauce: "))

                self.sauce_prices[sauce] = price

               

            for cheese in ['Mozzarella', 'Reggiano', 'Provolone', 'Parmesan']:

                price = float(input(f"Enter the price for {cheese} cheese: "))

                self.cheese_prices[cheese] = price

               

            for dough in ['ThinCrust', 'ThickCrust']:

                price = float(input(f"Enter the price for {dough} dough: "))

                self.dough_prices[dough] = price

           

            with open('prices.json', 'w') as f:

                prices = {

                    'pizza_prices': self.pizza_prices,

                    'sauce_prices': self.sauce_prices,

                    'cheese_prices': self.cheese_prices,

                    'dough_prices': self.dough_prices,

                }

                json.dump(prices, f)

 

    def get_pizza_price(self, pizza_type):

        return self.pizza_prices[pizza_type]

 

    def get_sauce_price(self, sauce_type):

        return self.sauce_prices[sauce_type]

 

    def get_cheese_price(self, cheese_type):

        return self.cheese_prices[cheese_type]

 

    def get_dough_price(self, dough_type):

        return self.dough_prices[dough_type]

 

def main():

    admin = Admin()

 

    print('Welcome to XYZ pizza creation software..........')

 

    p_choice = input('Choose pizza type \n 01. Greek \n 02. Chicago \n 03. NewYork \n 04. Sicilian: ')

    s_choice = input('Choose Sauce \n 01. PlumTomato \n 02. Marinara \n 03. Barbecue \n 04. Pumpkin: ')

    d_choice = input('Choose Dough \n 01. ThinCrust \n 02. ThickCrust: ')

    c_choice = input('Choose Cheese type \n 01. Mozzarella \n 02. Reggiano \n 03. Provolone \n 04. Parmesan: ')

 

    pizza_type = ''

    if p_choice == '1':

        pizza_type = 'Greek'

    elif p_choice == '2':

        pizza_type = 'Chicago'

    elif p_choice == '3':

        pizza_type = 'NewYork'

    elif p_choice == '4':

        pizza_type = 'Sicilian'

    else:

        print('Wrong choice')

 

    pizza_price = admin.get_pizza_price(pizza_type)

    sauce_price = admin.get_sauce_price('PlumTomato' if s_choice == '1' else 'Marinara' if s_choice == '2' else 'Barbecue' if s_choice == '3' else 'Pumpkin')

    cheese_price = admin.get_cheese_price('Provolone' if c_choice == '3' else 'Mozzarella' if c_choice == '1' else 'Reggiano' if c_choice == '2' else 'Parmesan')

    dough_price = admin.get_dough_price('ThinCrust' if d_choice == '1' else 'ThickCrust')

 

    total_price = pizza_price + sauce_price + cheese_price + dough_price

 

    if pizza_type == 'Chicago':

        total_price *= 0.95  

    elif pizza_type == 'Sicilian':

        total_price *= 0.96  

 

    if c_choice == '4':

        total_price *= 0.96  

 

    if s_choice == '3':

        total_price *= 0.975  

 

    print('Price of the requested pizza is $', round(total_price, 2))

    print("Name: Varnika \n Enrollment Number: E22MCAG0015")

 

if __name__ == '__main__':

    main()