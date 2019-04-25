from stationery.Stationery import Stationery


class Writing(Stationery):
    def __init__(self, type_of_goods, manufacture_of_goods, price_of_goods, quality_of_goods,
                 price_by_pencil, price_by_pen, type_of_notebooks):
        super().__init__(type_of_goods, manufacture_of_goods, price_of_goods, quality_of_goods)
        self.price_by_pencil = price_by_pencil
        self.price_by_pen = price_by_pen
        self.type_of_notebooks = type_of_notebooks

    def __str__(self):
        return super().__str__() \
               + "\nPrice_by_pencil:" + str(self.price_by_pencil) \
               + "\nPrice_by_pen: " + str(self.price_by_pen) \
               + "\nType of notebooks: " + str(self.type_of_notebooks)

    def __del__(self):
        pass
