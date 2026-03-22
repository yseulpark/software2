import random
class Car:
    def __init__(self,registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self,change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self,hours):
        self.travelled_distance += hours * self.current_speed

class Race:
    def __init__(self,name,distance_km,cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10,15)
            car.accelerate(change)
            car.drive(1)
    def print_status(self):
        for car in self.cars:
            print(f"{car.registration_number:<10} | Maximum speed: {car.maximum_speed:<12} | Current speed: {car.current_speed:<15} | Travelled distance: {car.travelled_distance:<10}")
    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False
cars =[]
for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100,200))
    cars.append(car)

race = Race("Grand Demolition Derby",8000,cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours +=1
    if hours % 10 == 0:
        print(f"Status at hour {hours}:")
        race.print_status()
print(f"Final status after {hours} hours:")
race.print_status()