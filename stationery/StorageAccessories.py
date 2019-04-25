from stationery.Stationery import Stationery


class StorageAccessories(Stationery):
    def __init__(self, type_of_goods, manufacture_of_goods, price_of_goods, quality_of_goods,
                 material_of_bag, price_by_toolbar, type_of_folder):
        super().__init__(type_of_goods, manufacture_of_goods, price_of_goods, quality_of_goods)
        self.material_of_bag = material_of_bag
        self.price_by_toolbar = price_by_toolbar
        self.type_of_folder = type_of_folder

    def __str__(self):
        return super().__str__() \
               + "\nMaterial of bag:" + self.material_of_bag \
               + "\nPrice by toolbar: " + str(self.price_by_toolbar) \
               + "\nType of folder: " + str(self.type_of_folder)

    def __del__(self):
        pass
