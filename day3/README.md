# DAY 3

### Part 1 Instructions

>Santa is delivering presents to an infinite two-dimensional grid of houses.

>He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

>However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

### Part 2 Instructions

>The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

>Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

>This year, how many houses receive at least one present?

### Part 1 Solution 

For this one, I felt like being a bit more fancy and so I made a Point class to make the code a bit cleaner / more
readable. Bear in mind that you definitely do not have to do it this way.

The Point class is fairly self explanatory, so I'll move on to the actual solution.

I first read in the solution, exactly like I did in Day 1's problems, and I then initialized four variables. First,
I wanted to store every point point Santa already visited in a list to make sure that we're not doubling up on a house.
Next, I made a variable to store the total unique houses Santa visits. Lastly, I stored Santa's previous x and y 
coordinates. 

The first part of the loop is fairly simple. I initialize a variable `point` to be equal to Santa's last known position.
From there, I move him north, east, south, or west depending on the instruction.

Next, I assume that Santa has never been to that point before and initialize `valid` to True. Then I check if his
current point is in the previous points array we made before, and if it is we set `valid` to False.

Then I check if `valid` is still true, and if it is we add Santa's current point to the visited points list, and increment
the total.

Last step is to set the previous coordinates equal to the current coordinates.

I also included some super fancy colored output, so be sure to use the included Virtual Environment when running this
(`source venv/bin/activate`)

### Part 2 Solution

It's basically the same problem as before, except this time there are two gift-givers (Santa and Robo-Santa), and each
instruction alternates between them.

This time, I had to store a couple more variables. Namely, I stored the current instruction count so that we could see
who it was for, and then I also stored to more previous coordinates for Robo-Santa. 

From here, it's pretty straightforward. I first check if we're on an even move, and if it is I set the variable
`is_robot` accordingly. 

Then I do the exact same things as before, except for that I check if it's Robo-Santa or Santa doing the actions
and edit the values accordingly.

Once again I also included some super fancy colored output, so be sure to use the included Virtual Environment when running this
(`source venv/bin/activate`)