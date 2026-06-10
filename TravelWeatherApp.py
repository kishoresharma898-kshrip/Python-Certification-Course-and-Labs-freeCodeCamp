'''
This is a lab activity given by freeCodeCamp in Python Certification course.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

1. You should create the following variables:
    distance_mi (a number representing the distance to travel in miles)
    is_raining (a boolean representing if the user is currently experiencing rainy weather)
    has_bike (a boolean representing if the user has a bicycle)
    has_car (a boolean representing if the user has a car)
    has_ride_share_app (a boolean representing if the user has an app that allows them to request a ride)
2. You should use conditional statements to determine whether commuting is possible based on the values of these variables.
3. You should use if, elif, and else statements to evaluate the distance categories in ascending order.
4. If distance_mi is a falsy value:
    You should print False.
5. If the distance is less than or equal to 1 mile:
    You should print True only if it is not raining.
    Otherwise, you should print False.
6. If the distance is greater than 1 mile and less than or equal to 6 miles:
    You should print True only if the person has a bike and it is not raining.
    Otherwise, you should print False.
7. If the distance is greater than 6 miles:
    You should print True if the person has a car or has a ride-share app.
    Otherwise, you should print False.'''

distance_mi = 6
is_raining = False
has_bike = False
has_car = True
has_ride_share_app = True

# Added additional print statements to check on the control-flow and for debugging.
# Uncomment the commented print statements to observe the control-flow and debug if there is/are any bug(s).
# Alter the values of variables to alter the control-flow.
# All tests passed.


if (not distance_mi):
    # print("In 1st if")
    print(False)

elif (distance_mi <= 1):
    if (not is_raining):
        # print("In 2nd if")
        print(True)
    else:
        # print("In 2nd if's else")
        print(False)

elif (distance_mi > 1 and distance_mi <= 6):
    if (has_bike and not is_raining):
        # print("In 3rd if")
        print(True)
    else:
        # print("In 3rd if's else")
        print(False)

elif (distance_mi > 6):
    if (has_car or has_ride_share_app):
        # print("In 4th if")
        print(True)
    else:
        # print("In 4th if's else")
        print(False)

# Output: 
# False
'''Since,
distance_mi = 6
is_raining = False
has_bike = False
has_car = True
has_ride_share_app = True

Therefore flow goes into 3rd if-else block where distance is greater than 1 and less than or equal to 6, but the rider has no bike to commute eventhough the whether is fine(i.e., no rain), and a car is an unecessary usage which costs more to travel a less distance.
'''

# Test results by fCC:
"""Passed:1. You should have a variable named distance_mi.
Passed:2. You should assign a number to your distance_mi variable.
Passed:3. You should have a variable named is_raining.
Passed:4. You should assign a boolean to your is_raining variable.
Passed:5. You should have a variable named has_bike.
Passed:6. You should assign a boolean to your has_bike variable.
Passed:7. You should have a variable named has_car.
Passed:8. You should assign a boolean to your has_car variable.
Passed:9. You should have a variable named has_ride_share_app.
Passed:10. You should assign a boolean to your has_ride_share_app variable.
Passed:11. You should use at least one if statement.
Passed:12. You should use at least one elif branch in your program.
Passed:13. You should use at least one boolean operator (and, or, or not) in your code.
Passed:14. You should use the print() function to display the result.
Passed:15. When distance_mi is a falsy value, the program should print False.
Passed:16. When the distance is 1 mile or less and it is not raining, the program should print True.
Passed:17. When the distance is 1 mile or less and it is raining, the program should print False.
Passed:18. When the distance is between 1 mile (excluded) and 6 miles (included), and it is raining with no bike, the program should print False.
Passed:19. When the distance is between 1 mile (excluded) and 6 miles (included), it is not raining but no bike is available, the program should print False.
Passed:20. When the distance is between 1 mile (excluded) and 6 miles (included), a bike is available, and it is not raining, the program should print True.
Passed:21. When the distance is greater than 6 miles and a ride share app is available, the program should print True.
Passed:22. When the distance is greater than 6 miles and a car is available, the program should print True.
Passed:23. When the distance is greater than 6 miles and no car nor a ride share app is available, the program should print False.
"""