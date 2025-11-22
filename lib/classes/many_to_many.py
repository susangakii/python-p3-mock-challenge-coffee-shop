class Coffee:
    all = []
    
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'):  # only set once (immutable)
            if isinstance(value, str) and len(value) >= 3:
                self._name = value
            else:
                raise ValueError("Name must be a string with at least 3 characters")
    
    #return all orders for this coffee
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    #return a unique list of customers who ordered this coffee (no duplicates)
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    #return the total number of orders for this coffee
    def num_orders(self):
        return len(self.orders())
    
    #return the average price of orders for this coffee
    def average_price(self):
        orders = self.orders()
        if orders:
            total = sum(order.price for order in orders)
            return total / len(orders)
        return 0


class Customer:
    all = []
    
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value): #mutable (can be changes once instantiated)
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
    
    #returns all orders for this customer
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    #returns unique list of coffees this customer has ordered
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    #creates a new order for this customer
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        #returns customer who spent the most on a given coffee
        customers_spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in customers_spending:
                    customers_spending[order.customer] = 0
                customers_spending[order.customer] += order.price
        
        if not customers_spending:
            return None
        return max(customers_spending, key=customers_spending.get)

   
class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not hasattr(self, '_price'):  # only set once (immutable)
            if isinstance(value, (int, float)) and 1.0 <= value <= 10.0:
                self._price = float(value)
            else:
                raise ValueError("Price must be a number between 1.0 and 10.0")
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Customer must be a Customer instance")
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("Coffee must be a Coffee instance")