class Order:
    def __init__(self,customer):
        self.customer = customer
        self.items = []
        self.total = 0
    
    def add_item(self, item, price):
        self.items.append(item)
        self.total += price
    
    def display_bill(self):
        print("\nCustomer:", self.customer)

        print("Items:")
        for item in self.items:
            print(item)
        
        print("Total:",self.total)

order = Order("Sarah")

order.add_item("Burger",200)
order.add_item("Fries",150)
order.add_item("Club Orange",100)

order.display_bill()