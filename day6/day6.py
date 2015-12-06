# Created on 12/6/15

"""
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.
"""

from termcolor import colored

def point_to_int(arr):
    for i in range(len(arr)):
                arr[i] = int(arr[i])
    return arr

if __name__ == '__main__':
    f_input = []
    with open("input.txt") as f:
        f_input = f.readlines()

    lights = {}
    for row in range(1000):
        for column in range (1000):
            lights[(row, column)] = False

    for line in f_input:
        line = line.split(" ")
        if line[0] + " " + line[1] == "turn on":
            start_point = line[2].split(",")
            start_point = point_to_int(start_point)

            end_point = line[4].split(",")
            end_point = point_to_int(end_point)

            for row in range(start_point[0], end_point[0] + 1):
                for column in range(start_point[1], end_point[1] + 1):
                    lights[(row, column)] = True

        elif line[0] + " " + line[1] == "turn off":
            start_point = line[2].split(",")
            start_point = point_to_int(start_point)

            end_point = line[4].split(",")
            end_point = point_to_int(end_point)

            for row in range(start_point[0], end_point[0] + 1):
                for column in range(start_point[1], end_point[1] + 1):
                    lights[(row, column)] = False

        elif line[0] == "toggle":
            start_point = line[1].split(",")
            start_point = point_to_int(start_point)

            end_point = line[3].split(",")
            end_point = point_to_int(end_point)

            for row in range(start_point[0], end_point[0] + 1):
                for column in range(start_point[1], end_point[1] + 1):
                    if lights[(row, column)]:
                        lights[(row, column)] = False
                    else:
                        lights[(row, column)] = True

    total = 0
    for row in range(1000):
        for column in range(1000):
            if lights[(row, column)]:
                total += 1

    print colored("TOTAL:", "magenta"),
    print(str(total))
