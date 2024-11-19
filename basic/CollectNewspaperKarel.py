"""
File: CollectNewspaperKarel.py
Name: Renee
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    move_to_news()
    pick_beeper()  # mission completed, turn back to home, facing East
    back_to_home()
    turn_right()  # facing East
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def walk():
    """
    Because it is the reverse route, the walking pathway is the same
    Pre-condition: Karel at the original point, facing East
    Post-condition: Karel at the mission point, facing South/ North
    """
    while front_is_clear():
        move()
    turn_right()
    move()


def cross():
    """
    Walk out the door, turn 90 degrees
    Pre-condition: Karel is facing South/ North
    Post-condition: Karel is facing East/ Western
    """
    turn_left()
    move()


def move_to_news():
    """
    Pre-condition: Karel at the original point (3,4), facing East
    Post-condition: Karel at the (6,3), facing East
    """
    walk()
    cross()


def back_to_home():
    """
    Pre-condition: Karel at the (6,3), facing East
    Post-condition: Karel at the original point (3,4), facing North
    """
    turn_left()
    cross()  # back to home
    walk()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
