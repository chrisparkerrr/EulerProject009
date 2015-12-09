# Euler Project Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.


I used Dickson's method to generate pythagorean triples and it is a LOT faster than a simple brute force.

Pure brute force ~ 12s
Dickson's method < 1ms
