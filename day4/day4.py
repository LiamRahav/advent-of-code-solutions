# Created on 12/5/15

"""
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

"""

from hashlib import md5
from termcolor import colored

if __name__ == '__main__':
    f_input = 'iwrupvqb' # input generated from site

    i = 0
    while True:
        i_string = str(i)

        combo_string = f_input + i_string

        md5_string = md5(combo_string.encode())
        hex_string = md5_string.hexdigest()

        if hex_string[:5] == '0' * 5:
            print colored("PASS:", "green"),
            print (hex_string)
            print colored("PASSING NUMBER:", "green"),
            print(i_string)
            break
        else:
            print colored("FAIL:", "red"),
            print(hex_string)

        i += 1

