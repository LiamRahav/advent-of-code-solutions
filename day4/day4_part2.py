# Created on 12/5/15

# Created on 12/5/15

from hashlib import md5
from termcolor import colored

if __name__ == '__main__':
    f_input = 'iwrupvqb' # input generated from site

    i = 0
    while True:
        i_string = str(i)

        combo_string = f_input + i_string

        hex_string = md5(combo_string.encode()).hexdigest()

        if hex_string[:6] == '0' * 6:
            print colored("PASS: " + hex_string, "green")
            print colored("PASSING NUMBER: " + i_string, "green")
            break
        else:
            print colored("FAIL: " + hex_string, "red")

        i += 1

