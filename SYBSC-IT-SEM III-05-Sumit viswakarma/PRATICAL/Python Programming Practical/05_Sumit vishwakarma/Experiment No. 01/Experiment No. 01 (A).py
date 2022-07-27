import datetime
name = input("enter your name : ")
age = int(input("enter your age : "))
print("your name is " + name)
year_now = datetime.datetime.now()
print(year_now.year)
print("your current age is " + str(int(age)) + " you will turn 100 in " + str(int(100 - age) + int(year_now.year)))
