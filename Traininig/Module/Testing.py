from Module.Orderlist import OrderList
from DatabaseConnection.DatabaseConnection import DatabaseConnection
from Module.Order import Order
from Module.Product import Product
from Controller.Controller import Customer

def main():

    jb = None
    ListID = Customer.getNewestIdforOrderListID()
    if ListID is not None:
        a = ListID.MyOrderList_ID
        c = a[2:10]
        b = int(c) + 1
        if 0 <= b <= 9:
            d = str(b)
            e = "LS0000000" + d
        elif 10 <= b <= 99:
            d = str(b)
            e = "LS000000" + d
        elif 100 <= b <= 999:
            d = str(b)
            e = "LS00000" + d
        elif 1000 <= b <= 9999:
            d = str(b)
            e = "LS0000" + d
        elif 10000 <= b <= 99999:
            d = str(b)
            e = "LS000" + d
        elif 100000 <= b <= 999999:
            d = str(b)
            e = "LS00" + d
        elif 1000000 <= b <= 9999999:
            d = str(b)
            e = "LS0" + d
        elif 10000000 <= b <= 99999999:
            d = str(b)
            e = "LS" + d
        jb = e
    else:
        jb = "LS00000001"

    print(jb)

getOrderId = Customer.getNewestIdforOrderID()
            if getOrderId is not None:
                    a = getOrderId.MyOrder_ID
                    c = a[2:10]
                    b = int(c) + 1
                    if 0 <= b <= 9:
                            d = str(b)
                            e = "BL0000000" + d
                    elif 10 <= b <= 99:
                            d = str(b)
                            e = "BL000000" + d
                    elif 100 <= b <= 999:
                            d = str(b)
                            e = "BL00000" + d
                    elif 1000 <= b <= 9999:
                            d = str(b)
                            e = "BL0000" + d
                    elif 10000 <= b <= 99999:
                            d = str(b)
                            e = "BL000" + d
                    elif 100000 <= b <= 999999:
                            d = str(b)
                            e = "BL00" + d
                    elif 1000000 <= b <= 9999999:
                            d = str(b)
                            e = "BL0" + d
                    elif 10000000 <= b <= 99999999:
                            d = str(b)
                            e = "BL" + d
                    odrerID = e
            else:
                    odrerID = "BL00000001"





main()





'''''
item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No"))
        self.tableWidget.setColumnWidth(0,50)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        self.tableWidget.setColumnWidth(1,450)
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        self.tableWidget.setColumnWidth(2,200)
        item = self.tableWidget.horizontalHeaderItem(3)
        self.tableWidget.setColumnWidth(3,200)
        item.setText(_translate("MainWindow", "Quantity"))
        self.label_total.setText(_translate("MainWindow", "Total"))

        category = "1"
        customer = Customer()
        products = customer.display_productbyCategory(category)

        row = 0
        self.tableWidget.setRowCount(200)
        for product in products:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(row+1)))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(product.Name))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(product.Price)))
            row += 1
'''''