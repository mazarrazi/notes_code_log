low = 1
high = 1000
print("the value is between {} and {} \n".format(low,high))
input("Press Enter to start")

attempts=1

while True:
    print(f"Guessing in the range of {low} and {high} \n")
    guess = low + (high - low)//2
    high_low=input(f"My guess is {guess}."
                   "Should I guess higher or lower."
                   "Press h for higher, l for lower or c if correct \n" ).casefold()

    if high_low == "h":
        low = guess+1
    elif high_low == "l":
        high = guess-1
    elif high_low == "c":
        print("I got it in {} attempts! \n".format(attempts))
    else:
        print("Enter h or l or c only")
	attempts = attempts+1
