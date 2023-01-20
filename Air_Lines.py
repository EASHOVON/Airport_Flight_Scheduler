import csv

from Air_Craft import Air_Craft


class Air_Lines:
    def __init__(self) -> None:
        self.air_crafts = None
        self.load_air_craft_data('./data/aircraft.csv')


    def load_air_craft_data(self,path):
        air_crafts = {}
        with open(path,'r') as file:
            lines = csv.reader(file)
            next(lines)
            for line in lines:
                air_crafts[line[0]] = Air_Craft(line[3],line[0],line[1],line[4])
        file.close()
        self.air_crafts = air_crafts


    def get_aircraft(self,aircraft_code):
        return self.air_crafts[aircraft_code]
    

    def get_aircraft_by_distance(self,distance):
        for aircraft in self.air_crafts.values():
            if aircraft.flight_range < distance:
                return aircraft
