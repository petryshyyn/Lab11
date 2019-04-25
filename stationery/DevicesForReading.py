from stationery.Stationery import Stationery


class DevicesForReading(Stationery):
    def __init__(self, type_of_goods, manufacture_of_goods, price_of_goods, quality_of_goods,
                 lamp, glasses, type_of_book):
        super().__init__(type_of_goods, manufacture_of_goods, price_of_goods, quality_of_goods)
        self.lamp = lamp
        self.glasses = glasses
        self.type_of_book = type_of_book

    def __str__(self):
        return super().__str__()\
               + "\nLamp:" + str(self.lamp)\
               + "\nGlasses: " + str(self.glasses)\
               + "\nType of goods: " + str(self.type_of_book)

    def __del__(self):
        pass
