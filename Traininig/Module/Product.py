


class Product:

    def __init__(self):
        self.Product_ID = None
        self.Name = None
        self.Price = None
        self.Category = None

    def set_Product_ID(self, Product_ID):
        self.Product_ID = Product_ID

    def set_Name(self, Name):
        self.Name = Name

    def set_Price(self, Price):
        self.Price = Price

    def set_Category(self, Category):
        self.Category = Category

    def get_Product_ID(self):
        return self.Product_ID

    def get_Name(self):
        return self.Name

    def get_Price(self):
        return self.Price

    def get_Category(self):
        return self.Category


