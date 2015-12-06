# Created on 12/5/15
"""
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
"""

if __name__ == '__main__':
    f_input = []
    with open("input.txt") as f:
        f_input = f.readlines()

    total = 0
    for string in f_input:
        check1 = False
        check2 = False
        check3 = True

        string = string.strip()

        # Check for 3 vowels
        counter = 0
        for c in string:
            if c in ('a', 'e', 'i', 'o', 'u'):
                counter += 1
        if counter >= 3:
            check1 = True

        last_letter = ''
        for c in string:
            if last_letter == c:
                check2 = True

            if last_letter == 'a' and c == 'b':
                check3 = False
            elif last_letter == 'c' and c == 'd':
                check3 = False
            elif last_letter == 'p' and c == 'q':
                check3 = False
            elif last_letter == 'x' and c == 'y':
                check3 = False

            last_letter = c

        if check1 and check2 and check3:
            print(string)
            total += 1

    print(total)
