# For Read CSV file
import csv

# Airport Class import
from Airport import Airport

# Import from math module
from math import radians,sin,cos,atan2,sqrt


# Making All Airport class for manage All Airport in the world
class AllAirports:
    def __init__(self) -> None:
        self.airports = None
        self.load_airport_data('./data/airport.csv')


    # For load all airport data
    def load_airport_data(self,path):
        airports = {}
        currency_rates = {}
        country_currency = {}

        # Getting currency name and rate
        with open("./data/currencyrates.csv","r") as file:
            lines = csv.reader(file)
            for line in lines:
                currency_rates[line[1]] = line[2]
        file.close()

        # Getting country with the help of currency name
        with open("./data/countrycurrency.csv","r") as file:
            lines = csv.reader(file)
            next(lines)
            for line in lines:
                country_currency[line[0]] = line[1]
        file.close()

        # Create Airport
        with open(path,'r',encoding="utf8") as file:
            lines = csv.reader(file)
            try:
                for line in lines:
                    country = line[3]
                    if country not in country_currency:
                        continue
                    currency = country_currency[country]
                    if currency not in currency_rates:
                        continue
                    rate = currency_rates[currency]
                    airports[line[4]] = Airport(line[4],line[1],line[2],line[3],line[6],line[7],rate)
            except KeyError as e:
                print("Key Error",e)
            self.airports = airports


    # Getting distance between two airports
    def get_distance_between_two_airports(self,lat1,lon1,lat2,lon2):
        radius = 6371
        lat_diff = radians(lat2-lat1)
        lon_diff = radians(lon2-lon1)
        arc = (sin(lat_diff/2) * sin(lat_diff/2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(lon_diff/2) * sin(lon_diff/2))
        c = 2 * atan2(sqrt(arc),sqrt(1-arc))
        distance = radius * c
        return distance
    
    # Distance between two airports
    def distance_between_two_airports(self,airport1_code,airport2_code):
        airport1 = self.airports[airport1_code]
        airport2 = self.airports[airport2_code]
        distance = self.get_distance_between_two_airports(airport1.lat,airport1.lon,airport2.lat,airport2.lon)
        return distance
    
    # Get Ticket Price
    def get_ticket_price(self,start,end):
        distance = self.distance_between_two_airports(start,end)
        airport1 = self.airports[start]
        fare = distance * airport1.rate
        return fare



