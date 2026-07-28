def fetch_valid_input():
    """Prompts user to guess a number and validates the guess."""
    UPPER_BOUND = 101
    done = False

    while not done:
            raw_input = (input("Guess a number from 1 to 100. "))
            if not raw_input.isnumeric():
                  print("Input is not a valid number. Please try again. ")
            else:
                  number = int(raw_input)
                  if number not in range(UPPER_BOUND):
                       print("Number is not in expected range. Please try again.")
                  else:
                        done = True

    return number

print(fetch_valid_input())