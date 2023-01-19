# For Read CSV file
import csv

# Airport Class import
from Airport import Airport


# Making All Airport class for manage All Airport in the world
class AllAirport:
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



