# DAY 2

### Part 1 Instructions

>The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

>Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

>All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

### Part 2 Instructions

>The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

>The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

>How many total feet of ribbon should they order?

### Part 1 Solution

This one is definitely harder than Day 1's, but it's still a fairly simple mathematical problem. This time I stored
the input line by line in an array called `f_input` using the `readlines()` function. 

From there, I looped through each
line and split the line further into length, width and height. So, say I got the input `1x2x3`, I would split it to
`[1, 2, 3]`. 

Next, I calculated the area of each side (no explanation needed). The next step was to find the amount of excess 
wrapping paper Santa needed, which was equal to the smallest side. My simple solution to this was to initialize
a variable `smallest` to the value 1000, and then check for the smallest side with three if statements. Not the most
elegant, but it's clear and it works.

The final step was to add the three areas together, multiply them by two (because it's a box) and then add on the 
amount of excess wrapping paper.

### Part 2 Solution

This is very similar to Part 1, except now it's about the ribbon needed to wrap the boxes rather than wrapping paper.

This time, the excess needed is equal to the perimeter of the smallest face rather than the area of the smallest side.
To solve this problem, I sorted the length, width, and height inside the array so that the smallest number appeared first
and so on (<3 `.sort()`). From there, I knew the slack was equal to the smallest number (`[0]`) x 2, plus the second
smallest number (`[1]`) x 2. 

Then I just added this excess ribbon value to the area and added that to the total. Last step was to output the total,
and the _voila_, we have our answer.