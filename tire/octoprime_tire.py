from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.__tire_wear = tire_wear

    def needs_service(self):
        total_wear = sum(self.__tire_wear)
        return total_wear >= 3
