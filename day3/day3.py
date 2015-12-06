# Created on 12/5/15

"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""

from termcolor import colored

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_north(self):
        self.y += 1

    def move_south(self):
        self.y -= 1

    def move_east(self):
        self.x += 1

    def move_west(self):
        self.x -= 1

if __name__ == '__main__':
    f = open("input.txt")
    f_input = f.read()
    f.close()

    visited_points = []
    total = 0
    prev_x = 0
    prev_y = 0
    for c in f_input:
        point = Point(prev_x, prev_y)
        if c == "^":
            point.move_north()
        elif c == "v":
            point.move_south()
        elif c == ">":
            point.move_east()
        elif c == "<":
            point.move_west()

        print colored("(%.1f, %.1f)" % (point.x, point.y), "magenta")

        valid = True
        for comparison_point in visited_points:
            if (comparison_point.x == point.x) and (comparison_point.y == point.y):
                valid = False

        if valid:
            visited_points.append(point)
            total += 1

        prev_x = point.x
        prev_y = point.y

    print colored("ANSWER:", "green"),
    print(total)