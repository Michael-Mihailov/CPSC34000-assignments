class Product:
    def __init__(self, prod_num:int, prod_name:str, price:float):
        self.set_product(prod_num, prod_name, price)

    def set_product(self, prod_num:int, prod_name:str, price:float):
        self.set_prod_num(prod_num)
        self.set_prod_name(prod_name)
        self.set_price(price)
    def set_prod_num(self, prod_num:int):
        self.__prod_num = prod_num
    def set_prod_name(self, prod_name:str):
        self.__prod_name = prod_name
    def set_price(self, price:float):
        self.__price = price

    def get_prod_num(self):
        return self.__prod_num
    def get_prod_name(self):
        return self.__prod_name
    def get_price(self):
        return self.__price

    def get_data(self):
        return ("%-6d %-25s %10.2f" % self.get_prod_num(), self.get_prod_name(), self.get_price())
    def get_stock_value(self):
        ...

class ProductionQuantity(Product):
    def __init__(self, prod_num:int, prod_name:str, price:float, quantity:int):
        super().__init__(prod_num, prod_name, price)
        self.set_quantity(quantity)

    def set_quantity(self, quantity:int):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def display_data(self):
        ...
    def get_stock_value(self):
        ...


class ProductPounds(Product):
    def __init__(self, prod_num:int, prod_name:str, price:float, pounds:float):
            super().__init__(prod_num, prod_name, price)
            self.set_pounds(pounds)
    
    def set_pounds(self, pounds:int):
        self.__pounds = pounds

    def get_pounds(self):
        return self.__pounds

    def display_data(self):
        ...
    def get_stock_value(self):
        ...