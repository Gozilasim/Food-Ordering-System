


class Data:

    Ordermode = None
    list_food_store = []
    list_price_store = []
    total_store = 0
    remark_store = None

    def set_Ordermode(self, Ordermode):
        self.Ordermode = Ordermode

    def get_Ordermode(self):
        return self.Ordermode


    def get_list_food(self):
        self.list_food_store

    def get_list_price(self):
        self.list_price

    def get_total(self):
        self.total_store

    def get_remark(self):
        self.remark_store


    def set_list_food(self, list_food_store):
        self.list_food_store = list_food_store

    def set_list_price(self, list_price_store):
        self.list_price_store = list_price_store

    def set_total(self, total_store):
        self.total_store = total_store

    def set_remark(self, remark_store):
        self.remark_store = remark_store