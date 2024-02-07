cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# == is a comparison operator that returns True if the values on the left and right side of the operator are equal.
# = is an assignment operator that stores a value in a variable.
# The if statement compares the value of car to the value 'bmw' with the equality operator (==).
# If the value of car is 'bmw', Python returns True, and the if statement passes the test.
# If the value of car is anything other than 'bmw', the test evaluates to False, and the code following the if statement is ignored.