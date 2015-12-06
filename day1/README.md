# DAY 1

### Part 1 Instructions

>Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

>Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

>Here's an easy puzzle to warm you up.

>Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

>An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

>The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

>To what floor do the instructions take Santa?

### Part 2 Instructions

>Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

>What is the position of the character that causes Santa to first enter the basement?

### Part 1 Solution

This one is fairly easy, and quite frankly it doesn't need much of an explanation. I read in all the parentheses from
`input.txt` into the variable `input_day1`, and from there it was smooth sailing. I looped through each paren, and then
incremented or decremented the total accordingly.

Easy problem, easy solution.

### Part 2 Solution

Again fairly easy. They want to know the first time Santa goes into the basement (floor -1 and beyond), so we basically
need to catch at what instruction we hit floor -1. To do this, I recorded the instruction we were on in the variable 
`pos` and from there I proceeded the same as I did in Part 1. The only exception is that I checked if the floor was
equal to -1 and then broke, and outputted the position rather than the floor number.