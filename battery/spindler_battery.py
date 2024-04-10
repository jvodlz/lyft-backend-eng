from battery.battery import Battery
from utils import add_years_to_date

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):
        service_threshold_date = add_years_to_date(self.__last_service_date, 3)
        return service_threshold_date < self.__current_date
    