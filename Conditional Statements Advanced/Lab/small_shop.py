from typing import List

class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item: {self.name}, Price: ${self.price:.2f}"

    def get_total_price(self, quantity):
        return self.price * quantity


class City:
    def __init__(self, cname, item_list):
        self.cname = cname
        self.item_list = item_list

    def __str__(self):
        return f"City: {self.cname}, {str(self.item_list)}"


sc = Item("coffee", 0.50)
pc = Item("coffee", 0.40)
vc = Item("coffee", 0.45)
sw = Item("water", 0.80)
pw = Item("water", 0.70)
vw = Item("water", 0.70)
sb = Item("beer", 1.20)
pb = Item("beer", 1.15)
vb = Item("beer", 1.10)
ss = Item("sweets", 1.45)
ps = Item("sweets", 1.30)
vs = Item("sweets", 1.35)
sp = Item("peanuts", 1.60)
pp = Item("peanuts", 1.50)
vp = Item("peanuts", 1.55)
sofia = City("Sofia", [sc, sw, ss, sp, sb])
plovdiv = City("Plovdiv", [pc, pw, ps, pp, pb])
varna = City("Varna", [vc, vw, vs, vp, vb])

cities = {sofia, plovdiv, varna}

item = input()
city = input()
quantity = float(input())

currentCity = [x for x in cities if x.cname == city][0].item_list
currentItem = [x for x in currentCity if x.name == item]
total = currentItem[0].get_total_price(quantity)
print(total)# [20, 40]
