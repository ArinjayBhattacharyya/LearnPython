age = int(input("How old are you?"))

# if age >= 16 and age <= 65:
if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Have a good day at home")

print("-" * 80)

if age < 16 or age > 65:
    print("Have a good day at home")
else:
    print("Have a good day at work")