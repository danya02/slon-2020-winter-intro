# TL;DR: `a^4 + b^4 + c^4 + 3 l^4 = a^2 (b^2 + c^2 - 3 l^2) + 3 l^2 (b^2 + c^2) + b^2 c^2`

AKA "How does GPS even work?"

Using [trilateration](https://en.wikipedia.org/wiki/True_range_multilateration#Two_Cartesian_dimensions,_two_measured_slant_ranges_(Trilateration)), of course.

I don't know how simplified this form is, but intuitively it seems like it cannot be simplified further: the triangle's vertex that's not on the X-axis has an awkward Y-coordinate, and the left side has a sum of the tesseracts of distances, which resembles the sum of squares needed to represent distance from coordinates on orthogonal axes.
