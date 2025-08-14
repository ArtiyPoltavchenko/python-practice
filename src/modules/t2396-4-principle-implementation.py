import logging

# Description:
# Product has it's attributes and methods.
# all attributes is covered with @property decorators to ensure input validation
# all input validations is covered with exeption handling
# 
# Subscription (child) class is inherited from Product (parent)
# - Has buy() method override, additional atribute & method.

class Product:
    products_sold = 0 #attribute, variable for the whole type of classes and inheritance

    def __init__(self, title, description, price, type="Product"):
        self._title = title # All atributes is non-public. Accessible by properties.
        self._type = type
        self._description = description
        self._price = price

    # ----- Decorators ------

    def stringExceptionHandler(func):
        def wrapper(self, value):
            try:
                if isinstance(value, str):
                    func(self, value)
                else:
                    raise TypeError(f"{func.__name__} argument must be a string")
            except TypeError as e:
                logging.warning(f"Invalid value in {func.__name__}: {e}")
        return wrapper

    # ----- Properties ------

    @property
    def title(self):
        return self._title

    @title.setter
    @stringExceptionHandler
    def title(self, title):
        self._title = title

    @title.deleter
    def title(self):
        del self._title
        print(f"{self._title} deleted")

    @property
    def type(self):
        return self._type

    @type.setter
    @stringExceptionHandler
    def type(self, type):
        self._type = type

    @property
    def description(self):
        return self._description

    @description.setter
    @stringExceptionHandler
    def description(self, description):
        self._description = description

    # ----- Methods ------

    def buy(self, user):
        print(f"User '{user}' has bought {self.type}: '{self.title}' for {self.price} CHF")
        Product.products_sold += 1 # or ++ ? which one will make it more obvious for reader ?

    
    def price(self):
        return self._price
    
    def set_price(self, price):
        try:
            if price > 0:
                self._price = price
            else:
                raise ValueError("price could not be less than 0")
        except ValueError as e:
            logging.warning(f"Invalid price: {e}. Setting price to 0.")
            self._price = 0
   
    

    def printProductsSold(self):
        print(f"Products already sold: {self.products_sold}")

    #acess to global class attribute
    @classmethod
    def getProductsSold(cls):
        return cls.products_sold
    
    # actions with global class attribute
    @classmethod
    def resetProductsSold(cls):
        cls.products_sold = 0
        print("Products sold counter is setted to 0")

    # no class/object dependencies - working solo (alone)
    @staticmethod
    def generateArticle(title, lastProductId):
        return (f"PI{title}ID{lastProductId + 1}")

# Class Inherited from Product. It is like a Product, but with date features.
class Subscription(Product):
    def __init__(self, title, description, price, days, type="Subscription"):
        super().__init__(title, description, price, type) 
        self.__days = days  

    # Additional attribute for Inherited class. With property wrap.
    @property
    def days(self):
        return self.__days
    
    # Days setter with greater than 0 validation + exeption handling
    @days.setter
    def days(self, days):
        try:
            if days > 0 :
                self.__days = days
            else: 
                raise ValueError("days could not be less than 0")
        except ValueError as e:
            logging.warning(f"Ivalid days: {e}. Setting days to 0")
            self.__days = 0

    # Polymorphism - ovverriding of parrent's method with different functionality
    def buy(self, user):
        print(f"User '{user}' has bought {self.type}: '{self.title}' for {self.price} CHF \n and it wil last for {self.days} days")
        Product.products_sold += 1

    # Additional method into Inherited class
    def extend(self, days):
        self.days += days
        print(f"The '{self.title}' subscription was extended for: {self.days} days")

# Objects initialization (e.g. recieved database package)
product = Product("Keyboard", "The buttons goes click", 150)
subscription1 = Subscription("Fresh Air", "Wind blow in your area every 30 sec", 300, 30)
subscription2 = Subscription("Coffee Everyday", "Wind blow in your area every 30 sec", 300, 30, "Waste of money")

#actions and use of Methods
product.buy("Tom")
product.printProductsSold()

subscription1.buy("Jim")
subscription1.extend(15)
subscription1.printProductsSold()

subscription2.buy("Beam")
subscription2.extend(20)
subscription2.printProductsSold()


# use of class method
Product.resetProductsSold()
print(Product.getProductsSold())

# Use of static method
print(Product.generateArticle("Screwdriver", 12400881))