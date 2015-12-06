# Created on 12/6/15


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
            lights[(row, column)] = 0

    for line in f_input:
        line = line.split(" ")
        if line[0] + " " + line[1] == "turn on":
            start_point = line[2].split(",")
            start_point = point_to_int(start_point)

            end_point = line[4].split(",")
            end_point = point_to_int(end_point)

            for row in range(start_point[0], end_point[0] + 1):
                for column in range(start_point[1], end_point[1] + 1):
                    lights[(row, column)] += 1

        elif line[0] + " " + line[1] == "turn off":
            start_point = line[2].split(",")
            start_point = point_to_int(start_point)

            end_point = line[4].split(",")
            end_point = point_to_int(end_point)

            for row in range(start_point[0], end_point[0] + 1):
                for column in range(start_point[1], end_point[1] + 1):
                    if lights[(row, column)] != 0:
                        lights[(row, column)] -= 1

        elif line[0] == "toggle":
            start_point = line[1].split(",")
            start_point = point_to_int(start_point)

            end_point = line[3].split(",")
            end_point = point_to_int(end_point)

            for row in range(start_point[0], end_point[0] + 1):
                for column in range(start_point[1], end_point[1] + 1):
                    lights[(row, column)] += 2

    total = 0
    for row in range(1000):
        for column in range(1000):
            total += lights[(row, column)]

    print colored("TOTAL:", "magenta"),
    print(str(total))
