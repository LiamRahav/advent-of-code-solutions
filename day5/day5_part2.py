# Created on 12/5/15

if __name__ == '__main__':
    f_input = []
    with open("input.txt") as f:
        f_input = f.readlines()

    total = 0
    for line in f_input:
        check1 = False
        check2 = False

        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                check1 = True
                break

        # For some semblance of speed, added a check to see if performing the second check is even worth it
        if check1:
            for i in range(len(line) - 1):
                pair = line[i] + line[i + 1]
                if line.count(pair) >= 2:
                    check2 = True
                    break

        if check1 and check2:
            total += 1

    print(total)


