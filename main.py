import time

seed = 0    # Defining seeds for the process() function to call
nextseed = 0


def process():  # Defines the conjecture and performs it
    global seed
    global nextseed
    while True:    # Seed input
        try:
            seed = int(input("Input a number to serve as the seed (INT ONLY): "))
            break
        except:
            print("Input an integer!")
    while seed != 1 and seed != -1:    # Loops until seed is either 1 or -1
        if (seed % 2) == 0:    # Checks for even numbers
            nextseed = int(seed / 2)
            seed = nextseed
            print(nextseed)
        else:   # Checks for odd numbers
            nextseed = (seed * 3) + 1
            seed = nextseed
            print(nextseed)
    print("The Collatz conjecture is still true!")
    input("[Press Enter to exit.]")


if __name__ == "__main__":  # Runs the script if it is being run directly, rather than being called from another script
    print("Welcome to 3Xplus1, made with <3 by WilliamAfton-codes")
    print("This is a demonstration program meant to test the Collatz conjecture, often known as 3x+1")
    print("[Negative numbers are buggy, may cause to infinite loops!]")
    time.sleep(1)   # Short break for effect

    process()
