low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press enter to start")

guesses\
    = 1
while True:
    print("\tGuessing in the range of {} 10 {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher lower? "
                     "Enter h or l, or c if my guess is correct"
                     .format(guess)).casefold()

    if high_low == "h":
        low = guess + 1

    elif high_low == "l":
        high = guess - 1

    elif high_low == "c":
        print("I got it it in {} guesses!".format(guesses))
        break

    else:
        print("Please enter h, l or c")

    # guesses = guesses + 1
    guesses += 1