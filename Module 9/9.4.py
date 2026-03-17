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

import random
cars =[]
for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100,200))
    cars.append(car)

race_finished = False

while not race_finished:
    for car in cars:
        car.accelerate(random.randint(-10,15))
        car.drive(1)
        if car.travelled_distance >=10000:
            race_finished = True
            break

for car in cars:
    print(f"{car.registration_number} | Maximum speed: {car.maximum_speed} | Current speed: {car.current_speed} | Travelled distance: {car.travelled_distance}")

