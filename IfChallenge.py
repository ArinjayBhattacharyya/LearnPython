name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome to the club 18-30 holidays, {0}".format(name))
else:
    print("i'm sorry, our holidays are only for cool people")
