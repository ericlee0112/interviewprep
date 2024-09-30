import collections

class UndergroundSystem:
    def __init__(self):
        self.ledger = collections.defaultdict(dict)
        # id -> ( startingStation, checkInTime )
        self.travelTimes = collections.defaultdict(list)
        # (startStation+endStation) -> (numberOfTrips, travelTimes)

        # when we check out, look up the stationName, and id to get the checkin time, and delete from hashmap 
        # calculate the traveltime and add to travelTimes hashmap

    def checkIn(self, id, startStation, checkInTime):
        self.ledger[id] = (startStation, checkInTime)
        
    def checkOut(self, id: int, endStation: str, checkOutTime: int) -> None:
        (originStation, checkInTime) = self.ledger[id]

        del(self.ledger[id])
        totalTravelTime = checkOutTime - checkInTime 

        # update self.travelTimes hashmap
        tripName = originStation + "->" + endStation
        if tripName not in self.travelTimes:
            self.travelTimes[tripName] = (1, totalTravelTime)
        else:
            (numberOfTrips, travelTimes) = self.travelTimes[tripName]
            self.travelTimes[tripName] = (numberOfTrips + 1, travelTimes + totalTravelTime)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tripName = startStation + "->" + endStation
        
        if tripName not in self.travelTimes:
            return 0

        (numberOfTrips, travelTimes) = self.travelTimes[tripName]

        return travelTimes / numberOfTrips
        
        
