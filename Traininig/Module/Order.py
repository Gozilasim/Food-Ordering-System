


class Order:

    def __init__(self):
        self.MyOrder_ID = None
        self.DateOfOrder = None
        self.TotalPrice = None
        self.Remark = None
        self.OrderMode = None

    def set_MyOrder_ID(self, MyOrder_ID):
        self.MyOrder_ID = MyOrder_ID

    def set_DateOfOrder(self, DateOfOrder):
        self.DateOfOrder = DateOfOrder

    def set_TotalPrice(self, TotalPrice):
        self.TotalPrice = TotalPrice

    def set_OrderMode(self, OrderMode):
        self.OrderMode = OrderMode

    def set_Remark(self, Remark):
        self.Remark = Remark

    def get_MyOrder_ID(self):
        return self.MyOrder_ID

    def get_DateOfOrder(self):
        return self.DateOfOrder

    def get_TotalPrice(self):
        return self.TotalPrice

    def get_OrderMode(self):
        return self.OrderMode

    def get_Remark(self):
        return self.Remark