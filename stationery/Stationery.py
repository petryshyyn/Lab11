class Stationery:

    def __init__(self, type_of_goods, manufacture_of_goods, price_of_goods, quality_of_goods):
        self.type_of_goods = type_of_goods
        self.manufacture_of_goods = manufacture_of_goods
        self.price_of_goods = price_of_goods
        self.quality_of_goods = quality_of_goods

    def __str__(self):
        return "\nType of goods:  " + self.type_of_goods\
               + "\nManufacture of goods: " + self.manufacture_of_goods\
               + "\nPrice of Goods: " + str(self.price_of_goods)\
               + "\nQuality of goods: " + str(self.quality_of_goods)

    def __del__(self):
        pass
