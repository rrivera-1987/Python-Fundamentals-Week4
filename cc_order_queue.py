class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
   
    def enqueue(self, items):
        self.items.append(items)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)
   
    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.order = Queue()
   
    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
           print("Sorry, we do not have that flavor.")
        elif scoops < 1 or scoops > 3:    
            print("Choose bewtween 1-3 scoops.")
        else:
            print("Order Created!")
            order = {"Customer": customer, "Flavor": flavor, "Scoops": scoops} 
            self.order.enqueue(order)
   
    def show_all_orders(self):
            print("\nAll pending ice cream orders: ")
            for i in self.order.items:
                customer = i["Customer"]
                flavor = i["Flavor"]
                scoops = i["Scoops"]
                print("Customer:", customer + ",", "Flavor:" , flavor + ",", "Scoops:", str(scoops))
   
    def next_order(self):
            print("\nNext order up!")
            i = self.order.dequeue()
            print("Customer:", i["Customer"] +",", "Flavor:", i["Flavor"], "Scoops:", i["Scoops"])
           


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()