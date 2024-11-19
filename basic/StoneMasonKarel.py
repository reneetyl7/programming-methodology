"""
File: StoneMasonKarel.py
Name: Renee
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    turn_left()
    while front_is_clear():
        up()
        down()


def turn_right():
    for i in range(3):
        turn_left()


def fill_beepers():
    """
    Fills a path with beepers.

    Pre-condition: The robot is on a clear path and may or may not be on a beeper.
    Post-condition: The robot has moved to the end of the path, placing a beeper at each position without one,
    including the last position.
    """
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
    if not on_beeper():
        # add on "not", take off the else function
        put_beeper()


def cross_arch():
    """
    The arch always in one size (3 steps far)
    Pre-condition: previous pillar
    Post-condition: next pillar
    """
    if front_is_clear():
        for i in range(4):
            move()


def up():
    """
    Pre-condition: Karel at the bottom of pillar, facing North
    Post-condition: Karel fixes the pillar at the top of pillar, facing South
    """
    fill_beepers()
    turn_right()
    cross_arch()  # to next pillar
    turn_right()


def down():
    """
    Pre-condition: Karel fixes the pillar at the top of pillar, facing South
    Post-condition: Karel at the bottom of pillar, facing North
    """
    fill_beepers()
    turn_left()
    cross_arch()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
