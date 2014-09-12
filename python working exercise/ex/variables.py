cars=100
space_in_a_car=4.0
drivers=30
passenger=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
#avg_pass_per_car=passenger/cars_driven
avg_pass_per_car=carpool_capacity/passenger

print "there are", cars,"cars available"
print "there are only",drivers, "drivers avilable"
print "there will be",cars_not_driven,"empty cars today"
print carpool_capacity
print passenger
print avg_pass_per_car
print "hey %s there." % "you"