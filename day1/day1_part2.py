# Created on 12/5/15


if __name__ == '__main__':
    floor_count = 0

    f = open("input.txt")
    input_day1 = f.read()
    f.close()

    pos = 1
    valid = True
    for c in input_day1:
        if c == "(":
            floor_count += 1
        elif c == ")":
            floor_count -= 1

        if floor_count < 0 and valid:
            print(pos)
            valid = False
        pos += 1

    print(floor_count)