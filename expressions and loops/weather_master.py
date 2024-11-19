"""
File: weather_master.py
Name: Renee
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

QUIT = -100  # Set the quit


def main():
    print("R \"Weather Master 4.0\"!")
    count = 1  # Initialize count to 1 to include the first input
    max_t = 0  # Max comparing
    min_t = 100  # min comparing, Initialise the first comparing number
    sum_t = 0  # sum all t, Initialise the standard
    alert = 0  # give a standard
    t = float(input("Next Temperature: (or  + " + str(QUIT) + " to quit)? "))

    if t != QUIT:
        sum_t = t  # put first entering number inside the loop to compare
        max_t = t
        min_t = t
        if t < 16:
            alert += 1

        while t != QUIT:
            t = float(input("Next Temperature: (or + " + str(QUIT) + " to quit)? "))
            if t != QUIT:
                sum_t = sum_t + t
                count += 1
                if max_t < t:
                    max_t = t
                if min_t > t:
                    min_t = t
                if t < 16:
                    alert += 1

            else:
                avg_t = sum_t / count
                print("Highest temperature = " + str(int(max_t)))
                print("Lowest temperature = " + str(int(min_t)))
                print("Average = " + str(avg_t))
                print(str(alert) + " cold day(s)")

    else:
        print("No temperatures were entered.")


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == "__main__":
    main()
