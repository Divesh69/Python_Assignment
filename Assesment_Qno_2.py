# Make a Python program that calculates the grades based on the
# percentage obtained in four different subjects. Use the following
# grading scheme: 80% and above is A+, 70% to 79% is A, 60% to 69% is
# A-, 50% to 59% is B, 40% to 49% is B-, and below 40% is Fail.

a = int(input("Enter your obtained marks in first subject out of 100: "))
b = int(input("Enter your obtained marks in second subject out of 100: "))
c = int(input("Enter your obtained marks in third subject out of 100: "))
d = int(input("Enter your obtained marks in fourth subject out of 100: "))
percentage = (a+b+c+d)/4
if percentage >= 80:
    print("You have obtained A+ grade.")
elif percentage >= 70 and percentage <=79:
    print("You have obtained A grade.")
elif percentage >= 60 and percentage <= 69:
    print("You have obtained A- Grade.")
elif percentage >= 50 and percentage <= 59:
    print("You have obtained B Grade.")
elif percentage >= 40 and percentage <= 49:
    print("You have obtained B- Grade.")
else:
    print("You failed in exam.")