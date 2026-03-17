class Car:
    def __init__(self,registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
car=Car("ABC-123",142)
print(f"The registration number of the car is {car.registration_number}.")
print(f"The car's maximum speed is {car.maximum_speed} km/h.")
print(f"Current speed of the car is {car.current_speed} km/h.")
print(f"Travelled distant of the car is {car.current_speed} km.")
