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
        self.travelled_distance = self.travelled_distance + hours * self.current_speed
car=Car("ABC-123",142)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current speed of the car is {car.current_speed} km/h.")
car.drive(2)
print(f"The car's travelled distance is {car.travelled_distance} km.")