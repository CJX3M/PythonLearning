class Elevator:
    def __init__(self, startingFloor) -> None:
        self.make = "The elevator company"
        self.floor = startingFloor

elevator = Elevator(1)
print(elevator.make)
print(elevator.floor)