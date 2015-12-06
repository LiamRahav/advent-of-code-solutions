# DAY 5

### Part 1 Instructions

>Santa needs help figuring out which strings in his text file are naughty or nice.

>A nice string is one with all of the following properties:

>It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.

>It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).

>It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

>How many strings are nice?

### Part 2 Instructions

>Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

>Now, a nice string is one with all of the following properties:

>It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).

>It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

>How many strings are nice under these new rules?

### Part 1 Solution

Well, the truth is that this solution is fairly straightforward, and if you've read any of my other solutions you 
probably understand the jist of how I'm getting the input and printing the output by now so... I'll just very briefly
cover both of these.

I looped through the input line by line, and each time I set three checks to False. I did a check for each one of the 
conditions above, and then set the variables to True accordingly. 

At the end of the loop, I check if all three checks are True. If they are, I increment the total of valid sentences.

### Part 2 Solution

The same as above, but with different checks. This one forced me to be a little bit more clever about how I was going
about checking for the 2 rules, because they weren't as "hardcodeable" as Part 1's checks.

When I first tried this problem, I didn't know the `count()` function existed, and so it became very messy and complicated
very quickly. Thankfully, after a teeny bit of Googling I found that function and was able to simplify my code a lot
and produce the right answer (69 😉).

I'm sure that if you use Python's included regex module, you can get this done a lot more cleanly, but I'm personally
not very familiar with it and didn't bother to learn as it was very late at night when I wrote this. So, I recommend
you try it that way if you've got some time to spare.