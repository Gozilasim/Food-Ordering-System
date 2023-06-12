


class OrderList:

    def __init__(self):
        self.MyOrderList_ID = None
        self.Quantity = None
        self.Subtotal = None
        self.MyOrder_ID = None
        self.Product_ID = None

    def set_Quantity(self, Quantity):
        self.Quantity = Quantity

    def set_Subtotal(self, Subtotal):
        self.Subtotal = Subtotal


    def set_MyOrder_ID(self, MyOrder_ID):
        self.MyOrder_ID = MyOrder_ID

    def set_MyOrderList_ID(self, MyOrderList_ID):
        self.MyOrderList_ID = MyOrderList_ID

    def set_Product_ID(self, Product_ID):
        self.Product_ID = Product_ID

    def get_MyOrder_ID(self):
        return self.MyOrder_ID

    def get_Quantity(self):
        return self.Quantity


    def get_MyOrderList_ID(self):
        return self.MyOrderList_ID

    def get_Product_ID(self):
        return self.Product_ID

    def get_Subtotal(self):
        return self.Subtotal