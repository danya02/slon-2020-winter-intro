# TL;DR: 432948736; but didn't find any solutions among the 42386000 tried options

AKA "Brute force and ignorance".

I couldn't figure out an answer to this one on my own.
Thus, this answer was found online.
Before you say that I am stolling this number I want to explain you a thing.

I didn't figure out a way to arrive at an analytic solution to this.
I was sure that there must be one, because computing it numerically is a nightmare.

According to the included program's performance on my machine (an [Intel Core i7-7700HQ](https://ark.intel.com/content/www/us/en/ark/products/97185/intel-core-i7-7700hq-processor-6m-cache-up-to-3-80-ghz.html), I'll have you know) with the clock rate set to the 3.8GHz limit, it'd take up to 107 days to find a solution.
This seems just a tad too long, so I didn't pursue this further.
(Technically speaking I could've set up a small distributed operation -- I do have a lot of computers, and all their powers combined would probably have helped -- but I also wasn't sure that my program is correct, so I thought that that may be too much of a waste of time than is required at Slon.)

I had some random ideas that for discovering an easier way to solve it along the way. One was to consider that the number we are looking for must be divisible by 2 -- unfortunately that didn't go far as the same argument does not extend far beyond that -- it also must be divisible by 4, but it may not be by 8. Another was related to binary counting -- `2^n` is `'0b1'+n*'0'` after all -- only that doesn't work either: `0b10` is 2, and `0b1010` is 10 -- but 10 does not end in 2.

So I tried looking for solutions online -- surely someone else has discovered a better way? Turns out, [they have](http://oeis.org/A064541), but I can't really figure out how they have done it. Thus, the answer is here, but I can't explain nor replicate it.
