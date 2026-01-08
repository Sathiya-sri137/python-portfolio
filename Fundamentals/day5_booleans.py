#Day 5 - Booleans and Conditionals
is_student = True
has_id = False
print(is_student)
print(has_id)
age = 18
print(age > 18)
print(age == 19)
print(age != 20)
print(age <= 17)
if age >=18:
    print("You are eligible to vote")
sales = 45000
if sales >= 50000:
    print("Profit")
else:
    print("Loss")
score = 75
if score >=90:
    print("Grade A")
elif score >=70:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")
is_raining = False
if not is_raining:
    print("You can go out")
else:
    print("Take a Umbrella")
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's a Holiday")
else:
    print("It's a Weekday")

