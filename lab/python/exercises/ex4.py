cars = 100 # Sets a value on the variable cars
space_in_a_car = 4.0 # decides how many seats it is in a car
drivers = 30 # number of drivers 
passengers = 90 # number of passengers
cars_not_driven = cars - drivers # defines cars not driven
cars_driven = drivers # cars driven is the same amount as drivers.
carpool_capacity = cars_driven * space_in_a_car # carpool capacity is number of cars driven * room in car
average_passengers_per_car = passengers / cars_driven # gets the average passenger per car.


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


#Traceback (most recent call last):
 #     File "ex4.py", line 8, in <module>
 #       average_passengers_per_car = car_pool_capacity / passenger
 #   NameError: name 'car_pool_capacity' is not defined
# says what file, wich line the error is. displays the line the error is in, and says that it is a NameError and explains that car_pool_capacity is not defined

