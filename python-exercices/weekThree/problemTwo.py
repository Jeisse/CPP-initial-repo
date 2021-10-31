# Problem 2: Write an application that displays the recommended
# weight given the users age and height (in centimeters) using the following formula:
# RW = (height - 100 + age % 10) * 0.90


print("Welcome to the app where you can check your recommended weight. ")
userAge = int(input(" what is your age? "))

# TODO include validation here in case user input Float
userHeight = int(input("what is your height? "))

rw = (((userHeight - 100) + (userAge % 10)) * 0.90)

print("Your recommended weight is: " + str(rw))
