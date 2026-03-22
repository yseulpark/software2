class Elevator:
    def __init__(self,bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
    def go_to_floor(self,target_floor):
        if target_floor > self.top or target_floor < self.bottom:
            print("Invalid floor.")
            return
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor +=1
            print(f"Currently at floor {self.current_floor}.")
    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Currently at floor {self.current_floor}.")
class Building:
    def __init__(self,bottom,top,num_elevators):
        self.bottom = bottom
        self.top = top
        self.num_elevators = num_elevators
        self.elevators = []

        for i in range(num_elevators):
            elevator = Elevator(bottom,top)
            self.elevators.append(elevator)
    def run_elevator(self,num_elevator,target_floor):
        if num_elevator < 1 or num_elevator > len(self.elevators):
            print ("Invalid elevator number")
            return
        elevator = self.elevators[num_elevator-1]
        elevator.go_to_floor(target_floor)

building = Building(1,20,4)
building.run_elevator(3,16)


