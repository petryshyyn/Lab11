from stationery.StorageAccessories import StorageAccessories
from stationery.DevicesForReading import DevicesForReading
from stationery.Writing import Writing
from stationery.enums.Quality import Quality
from stationery.enums.Book import Book
from stationery.enums.Folder import Folder
from stationery.enums.Notebook import Notebook
from stationeryManager.StationeryManagerImpl import StationeryManagerImpl


def main():

    stationery_manager = StationeryManagerImpl()
    device_for_reading = DevicesForReading("Linz", "Mizar", 200, Quality.NORMAL, True, False, Book.PUBLICATIONS_YEAR)
    storage_accessories = StorageAccessories("Box", "Optima", 180, Quality.GOOD, "Cardboard", 30.5, Folder.COLOR)
    writing = Writing("Pen", "Cabinet", 100, Quality.BEST, 20.5, 10.5, Notebook.BRAND)
    stationery_manager.add_element_to_list(device_for_reading)
    stationery_manager.add_element_to_list(storage_accessories)
    stationery_manager.add_element_to_list(writing)

    print(stationery_manager.sort_by_price(False))
    print(stationery_manager.sort_by_price(True))
    print(stationery_manager.sort_by_type(False))
    print(stationery_manager.sort_by_type(True))

    print(stationery_manager.find_for_school_children(Quality.NORMAL))
    print(stationery_manager.find_for_senior_pupil(Quality.BEST))
    print(stationery_manager.find_for_student(Quality.GOOD))
    stationery_manager.show_elements_inl_list()


main()
