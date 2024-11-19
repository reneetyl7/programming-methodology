"""
File: extension1_MidpointKarel.py
Name: Renee
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.

-> Limit the area and find the midpoint
"""

from karel.stanfordkarel import *


def main():
    put_end_beepers()
    while front_is_clear():
        take_last_beeper_west()
        take_last_beeper_east()


def put_end_beepers():
    """
    Pre-condition: no beeper
    Post-condition: Karel puts beepers on each side except the most left/ right points.
    """
    if front_is_clear():
        move()
        put_beeper()
        while front_is_clear():
            move()
    turn_around()
    if front_is_clear():
        move()
        put_beeper()


def take_last_beeper_west():
    """
    Check the west side position
    Pre-condition: half of west side except the end point has beepers
    Post-condition: remove the west side beeper step-by-step
    """
    if facing_west():
        move()
        if not on_beeper():
            put_beeper()
        turn_around()
        move()
        pick_beeper()
        turn_around()
        move()
        move()
    detect_beeper()
    turn_around()


def take_last_beeper_east():
    """
    Check the east side position
    Pre-condition: half of east side except the end point has beepers
    Post-condition: remove the east side beeper step-by-step
    """
    if facing_east():
        pick_beeper()
        move()
        if not on_beeper():
            put_beeper()
        move()
        detect_beeper()
        turn_around()


def detect_beeper():
    """
    Checkpoint: Collect the target beepers (guide the Karel)
    Pre-condition: Karel hit the wall
    Post-condition: Karel moves to the indicating position
    """
    while not on_beeper():
        if front_is_clear():
            move()
        if not front_is_clear():
            turn_around()
            while front_is_clear():
                if not on_beeper():
                    move()


def turn_around():
    """
    Pre-condition: Karel at the original place
    Post-condition: Karel turns to the opposite side
    """
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    execute_karel_task(main)
