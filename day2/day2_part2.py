# Created on 12/5/15

"""
--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.
"""

if __name__ == '__main__':
    f = open("input.txt")
    f_input = f.readlines()
    f.close()

    total = 0
    for line in f_input:
        line = line.strip().split("x")
        for i in range(len(line)):
            line[i] = int(line[i])

        line.sort()
        additional = line[0] * 2
        additional += line[1] * 2

        total += (line[0] * line[1] * line[2]) + additional

    print(total)

