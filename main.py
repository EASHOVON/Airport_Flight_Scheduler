# For Main Operation
from TravelAgent import TravelAgent

    
def main():
    travel_agent = TravelAgent("Go Jaan")
    trip_info1 = travel_agent.set_trip_one_city_one_way("DAC","PRA","07/05/2025")
    # print(trip_info1.aircraft)
    # print("Price",trip_info1.price)
    trip_cities = ['DUB','LHR','SYD','JFK']
    trip_info2 = travel_agent.set_trip_muli_city_flexible_route(trip_cities,'05/05/2025')
    print("Price of this Trip->",trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)


if __name__ == '__main__':
    main()