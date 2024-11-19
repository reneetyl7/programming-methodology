"""
File: MidpointKarel.py
Name: Renee
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.

-> Put both sides and check the midpoint
"""

from karel.stanfordkarel import *


def main():
    put_beeper()
    if front_is_clear():
        move()
        if front_is_clear():
            find_midpoint()
            cleanup_up_beepers()
        else:
            turn_around()
        middle()


def turn_around():
    """
    Pre-condition: Karel at the original place
    Post-condition: Karel turns to the opposite side
    """
    turn_left()
    turn_left()


def turn_and_move():
    """
    Pre-condition: Karel hit the wall
    Post-condition: Karel turn opposite and move
    """
    turn_around()
    move()


def move_to_end():
    """
    Pre-condition: Karel at the original place
    Post-condition: Karel put beepers on the first/end point
    """
    while front_is_clear():
        move()
    put_beeper()
    turn_and_move()


def middle():
    """
    skip all empty sites and move
    """
    while not on_beeper():
        move()


def find_midpoint():
    """
    make sure Karel can find the middle point
    """
    move_to_end()
    while not on_beeper():  # label the rest of empty site (not include first & end point)
        is_mid()
        fill_beeper()


def is_mid():
    """
    On beeper reaction
    checkpoint 1: fill beepers on both sides except middle
    """
    move()
    if on_beeper():
        turn_and_move()
        put_beeper()


def fill_beeper():
    """
    No beeper reaction
    checkpoint2: make sure put beeper side by side
    """
    if not on_beeper():
        while not on_beeper():
            move()
        turn_and_move()
        put_beeper()
        move()


def pick_rest_beepers():
    """
    Cleaning reaction
    Pre-condition: the line fill with beepers
    Post-condition: check each step and take the beepers
    """
    while front_is_clear():
        move()
        pick_beeper()


def cleanup_up_beepers():
    """
    Cleaning checkpoint
    Pre-condition: both sides have beepers
    Post-condition: clean beeper side by side
    """
    pick_rest_beepers()
    turn_around()
    middle()
    pick_rest_beepers()
    turn_around()


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    execute_karel_task(main)
