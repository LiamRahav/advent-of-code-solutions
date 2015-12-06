# Created on 12/5/15
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

from day3 import Point

if __name__ == '__main__':
    f = open("input.txt")
    f_input = f.read()
    f.close()

    visited_points = []

    counter = 0
    total = 0
    prev_x = 0
    prev_y = 0
    prev_x_robot = 0
    prev_y_robot = 0
    for c in f_input:
        is_robot = False
        point = Point(prev_x, prev_y)
        if counter % 2 != 0:
            is_robot = True
            point = Point(prev_x_robot, prev_y_robot)

        if c == "^":
            point.move_north()
        elif c == "v":
            point.move_south()
        elif c == ">":
            point.move_east()
        elif c == "<":
            point.move_west()

        if is_robot:
            print("ROBOT: (%.1f, %.1f)" % (point.x, point.y))
        else:
            print("SANTA: (%.1f, %.1f)" % (point.x, point.y))

        valid = True
        for comparison_point in visited_points:
            if (comparison_point.x == point.x) and (comparison_point.y == point.y):
                valid = False

        if valid:
            visited_points.append(point)
            total += 1

        if is_robot:
            prev_x_robot = point.x
            prev_y_robot = point.y
        else:
            prev_x = point.x
            prev_y = point.y

        counter += 1

    print(total)
