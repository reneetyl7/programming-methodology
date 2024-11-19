"""
File: extension2_MidpointKarel.py
Name: Renee
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.

-> Fill whole line (the midpoint has double beepers)and take one beeper
at each position. Then, Karel moves back to the midpoint.
"""

from karel.stanfordkarel import *


def main():
    if front_is_clear():
        move_to_end()
        put_beepers_down()  # mark whole line with beepers
        turn_around()
        move()
        put_beeper()  # midpoint label
        turn_around()
        go_to_wall()
        turn_around()
        clean_up_beepers()  # hit the wall, facing east
        turn_around()
        middle()  # move back to midpoint
    else:
        put_beeper()


def move_to_end():
    """
    Pre-condition: Karel at the original place
    Post-condition: Karel put beepers on the first/end point
    """
    go_to_wall()
    put_beeper()
    turn_around()
    go_to_wall()
    put_beeper()
    turn_around()
    move()


def go_to_wall():
    """
    Moving reaction:
    let Karel move if front is clear
    """
    while front_is_clear():
        move()


def put_beepers_down():
    """
    Pre-condition: beeper only show up at the most left/ right side
    Post-condition: put beeper side by side except there is beeper
    """
    while not on_beeper():
        move()
        if on_beeper():
            turn_around()
            move()
            put_beeper()
            move()


def clean_up_beepers():
    """
    Pre-condition: beepers fill the line
    Post-condition: clean up the beepers
    """
    while front_is_clear():
        if on_beeper():
            pick_beeper()
        move()
    pick_beeper()


def middle():
    """
    Pre-condition: Karel at the end position
    Post-condition: Karel stands at the midpoint
    """
    while not on_beeper():
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
