# DAY 4

### Part 1 Instructions

>Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

>To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

### Part 2 Instructions

>Now find one that starts with six zeroes.

### Part 1 Solution

This is this first problem which I had trouble with. I'm very unfamiliar with hashing and such, and so this was a bit
of a learning experience for me. Apologies in advanced if my solution isn't 10/10.

The first thing I did was hard code in the input given to me on http://adventofcode.com/day/4 into `f_input`. From there,
I set the variable `i` to zero and began an infinite loop. We needed to find the hash of the key + the lowest possible
number that started with 5 zeroes in hex. Whew, that's a lot to do. Thankfully, I found that the code for this was
rather simple.

The first thing I did was convert the current number into a string, so that we could do all sorts of manipulation on it.

Next, I combined the two strings (the key and the number) into one string so that I could then test if it had 5 leading
zeroes.

I made the string into it's MD5 hash by running `md5(combo_string.encode())`, and from there I found the hex verison
of that string by running `md5_string.hexdigest()`. It was a lot easier than I thought, as I said before. Just took a 
bit of Googling.

From there I just did a standard Pythonic string slice to see if the first 5 characters were zeroes and made some fancy
output using the `termcolor` module. (activate the Virtual Environment by running `$ source venv/bin/activate` in order
to see it)

### Part 2 Solution

Well, not much explanation here. I just changed where I was checking for 5 zeroes to 6 zeroes and let it run. It takes
an extremely long time to run and makes my laptop's fan go crazy after the first 30-45 seconds, but it works.