# Problem 4: Having just started college, Bob has been busy looking for a part-time job to fund his new college social
# life and after only two weeks of looking he has managed to get two job offers! Each job comes with different hours,
# basic rates of pay and over-time rates so he needs to work out which would get him the most money.
# Develop an application that would allow Bob to enter his basic pay rate, his number of regular hours work per week
# and his number of overtime hours per week.
# The application should then calculate and display Bobs total basic pay
# for the week, his overtime pay for the week and his total pay including overtime.
# Note: The overtime rate is 1.5 times the basic rate of pay.

while True:
    basicPayRate = float(input("What is the basic pay rate for this job? "))
    hoursPerWeek = float(input("What is the number of regular hours work per week for this job? "))
    overtimeHoursPerWeek = float(input("What is the number of regular hours work per week for this job? "))

    totalBasicPay = ((hoursPerWeek * basicPayRate) + (overtimeHoursPerWeek * (basicPayRate * 1.5)))

    print("Your total basic pay per week is: " + str(totalBasicPay))

    print("")
