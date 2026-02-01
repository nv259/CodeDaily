class RideSharingSystem:

    def __init__(self):
        self.riders = SortedList([])
        self.drivers = SortedList([])
        self.time = 0

    def addRider(self, riderId: int) -> None:
        self.riders.add((self.time, riderId))
        self.time += 1

    def addDriver(self, driverId: int) -> None:
        self.drivers.add((self.time, driverId))
        self.time += 1

    def matchDriverWithRider(self) -> List[int]:
        if len(self.riders) and len(self.drivers):
            driverId = self.drivers[0]
            riderId = self.riders[0]
            self.drivers.remove(driverId)
            self.riders.remove(riderId)
            
            return [driverId[1], riderId[1]]
        else:
            return [-1, -1]
        
    def cancelRider(self, riderId: int) -> None:
        for time, id in self.riders:
            if id == riderId:
                self.riders.discard((time, riderId))
        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)