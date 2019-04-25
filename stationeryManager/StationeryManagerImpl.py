class StationeryManagerImpl:
    stationery_list = []

    def __init__(self):
        pass

    def add_element_to_list(self, stationery):
        self.stationery_list.append(stationery)

    def sort_by_price(self, reverse):
        return sorted(self.stationery_list, key=lambda stationery: stationery.price_of_goods, reverse=reverse)

    def sort_by_type(self, reverse):
        return sorted(self.stationery_list, key=lambda stationery: stationery.type_of_goods, reverse=reverse)

    def find_for_school_children(self, quality_name):
        return list(filter(lambda stationary: stationary.quality_of_goods == quality_name, self.stationery_list))

    def find_for_senior_pupil(self, quality_name):
        return list(filter(lambda stationary: stationary.quality_of_goods == quality_name, self.stationery_list))

    def find_for_student(self, quality_name):
        return list(filter(lambda stationary: stationary.quality_of_goods == quality_name, self.stationery_list))

    def show_elements_inl_list(self):
        for elements in self.stationery_list:
            print(elements)

    def __del__(self):
        pass
