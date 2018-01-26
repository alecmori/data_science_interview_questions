Problem
=======

Let's say I gave you three images for the same search result, and I
asked you which one to show if you wanted that search result to have
the highest click through rate. You show each image *10* times, and

* The first gets clicked *2* times.
* The second gets clicked *7* times.
* The third gets clicked *8* times.

Your gut instinct might say "Well, I'm pretty sure the first one is
worse than the second and third, but I'm not too sure which one of
those two is better." However, if we showed each image *1000* times, 
and saw that

* The first gets clicked *200* times,
* The second gets clicked *700* times,
* The third gets clicked *800* times,

then you might be more assured that the last is best. Why? Because we
can frame each one of these options as a probability distribution, with
the variance depending on how many times you have chosen that particular
option.

![alt text](https://github.com/alecmori/data_science_interview_questions/multi_armed_bandit/images/three_different_choices.png "Three options, each chosen 10 times")

However, we showed the first image *1000* times, when we were confident
that it was worse than the other two after *10*. How can we decide to
stop showing an option after it doesn't work?

Multi-Armed Bandit
==================

Hello.
