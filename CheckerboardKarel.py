"""
File: CheckerboardKarel.py
Name: Renee
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    check_direction()  # Meet the wall, turn left
    if front_is_clear():
        put_beeper()
    while front_is_clear():
        fill_one_line()


def turn_right():
    """
    Pre-condition: Karel doesn't move
    Post-condition: Karel turns right
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    Pre-condition: Karel at the original place
    Post-condition: Karel turns to the opposite side
    """
    turn_left()
    turn_left()


def check_direction():
    """
    Pre-condition: facing East
    Post-condition: facing North (if meet the wall)
    """
    if not front_is_clear():
        turn_left()


def beepers_guide():
    """
    control Karel second move, avoid hitting the wall (include 2 checkpoints)
    """
    if facing_east():
        turn_around()  # checkpoint1
        move()
        if not on_beeper():
            turn_around()
            move()
            put_beeper()
            turn_left()
            if front_is_clear():  # checkpoint2: whether Karel meet the end point
                move()
                turn_left()
                move()
            else:
                turn_right()  # End point action
        else:
            turn_around()
            move()
            turn_left()
            if front_is_clear():  # whether Karel meet the end point
                move()
                turn_left()
            else:
                turn_right()  # End point action
        fill_one_line()

# if meet the even street, copy facing east coding checkpoint2
    if facing_west():
        if right_is_clear():
            turn_right()
            move()
            turn_right()
            fill_one_line()


def fill_one_line():
    """
    Pre-condition: no beepers/ reaction
    Post-condition: 1) put beepers in the right place and move one step
                    2) second step will be checked
    """
    while front_is_clear():
        put_beeper()
        if front_is_clear():
            move()
            if front_is_clear():  # double check if Karel meet the wall
                move()
            if not front_is_clear():  # if hit the wall
                beepers_guide()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
