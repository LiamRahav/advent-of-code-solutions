# DAY 6

### Part 1 Instructions

>Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

>Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

>Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

>To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

>After following the instructions, how many lights are lit?

### Part 2 Instructions

>You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

>The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

>The phrase turn on actually means that you should increase the brightness of those lights by 1.

>The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

>The phrase toggle actually means that you should increase the brightness of those lights by 2.

>What is the total brightness of all lights combined after following Santa's instructions?

### Part 1 Solution

Once again, I'm sure that regular expressions could save you some time here, but I wrote this solution right after I 
wrote Day 5's so I was even more tired and unwilling to learn. 

I'm also going to be shifting to more of an explanatory method of writing these rather than a step by step method, kind of
like I did in Day 5.

So, let's get down to it. The main problem I faced with this one was how I was going to model the data (a 1000 x 1000
field of lights, that can be on or off). After a bunch of trial and error, I settled on a dictionary that used the
XY coordinates as the key and had the boolean as the value.

From there, the solution was straightforward. I did some string splitting and whatnot to get the value I needed,
and then looped from the start point to the end point and performed the specified instruction until they were all 
processed.

Once everything was done, I just looped through it one last time and checked for which lights were on and added that
number to the total, which I outputted right after.

### Part 2 Solution

Part 2 basically changed the data from being in Boolean form (on / off) to Int form (0-∞) where the number represents
the light's brightness. Still fairly straightforward though.

I just copy pasted my code and changed the Booleans to Ints and I was done. 

Once again, these probably aren't the fastest solutions. A friend of mine was telling he was going to use a quad segment tree
for this problem, and I'm sure that's a better way of doing it. Thankfully, however, unlike the [USACO](http://usaco.org/) competition, 
Advent of Code doesn't care about how long it takes your code to run, just whether or not it produces the right
output. 