from requests import get, post
from datetime import date, timedelta, datetime
from attributes import stations, passengers, Trip

URL = "https://www.vr.fi/api/v7"

def generateParams(depStation, arrStation, passengerType, depTime):
    return {
        "operationName": "searchJourney",
        "variables": {
            "filters": [],
            "arrivalStation": arrStation,
            "departureStation": depStation,
            "departureDateTime": depTime.isoformat(),
            "passengers": [
                {
                    "type": passengerType,
                    "wheelchair": False,
                    "vehicles": []}],
            "placeTypes": [
                "SEAT",
                "CABIN_BED"]},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "137b82599f60fe662143194950e3a49469822bdddea4c1e360948cb979e946bd"}}}

# params = {
# "operationName":123
# }

depStation = stations.TPE
arrStation = stations.HKI
depDate = date(year=2025, month=6, day=30)
passenger = passengers.student

# print(depDate+ timedelta(days=1))

# json = generateParams(depStation, arrStation, passenger, depDate)
# ret = post(URL, json=json, headers={"content-type": "application/json"})
# for trip in ret.json()["data"]["searchJourney"]:
#     print(Trip(trip))

for ii in range(30):
    thisDate = datetime.now() +timedelta(days=ii)
    print(thisDate.date(), end=" ")
    
    json = generateParams(depStation, arrStation, passenger, thisDate)
    ret = post(URL, json=json, headers={"content-type": "application/json"})
    for tripRaw in ret.json()["data"]["searchJourney"]:
        trip = Trip(tripRaw)
        printStr = f"({trip.departureTime.time()},{trip.arrivalTime.time()}, {trip.totalPrice/100})"
        print(printStr, end=" ")
    print()