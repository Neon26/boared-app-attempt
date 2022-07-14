from time import sleep
import requests
from colorizer import *

class bored():
    def __init__(self):
        self.activity = ""
        self.type = ""
        self.participants = ""
        self.price = ""

    def bored_app(self):
        response = requests.get(f'/api/activity?minprice={bored.min_price()}&maxprice={bored.max_price()}')      
        if not response.ok:
            return False
        data = response.json()
        print(data)

        self.activity = data["activity"]
        self.type = data["type"]
        self.participants = data["participants"]
        self.price = data["price"]
        print(data)
        return

        
    
    def min_price():
        min_price = input_green("What is the min amount of money you are willing to spend on a daily activity?")
        return

    def max_price():
        max_price = input_green("What is the max amount of money you are willing to spend on a daily activity?")
        return


bored.min_price()
bored.max_price()
bored.bored_app(sleep)
    