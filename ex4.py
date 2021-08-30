#car pool capacity was defined & named "carppol_capacity" instead of "car_pool_capacity" like it was used, which is not declared
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
#assigned as the cars minus drivers
cars_not_driven = cars - drivers
#setting to the same value as drivers
cars_driven = drivers
#setting to cars driven multiplied by space in a car
carpool_capacity = cars_driven * space_in_a_car
#setting to passengers divided by cars driven
average_passengers_per_car = passengers / cars_driven

#printing the values with descriptions
print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")