# Day 19

THIS IS THE MOST TIRING DAY EVER

I got stuck at the indexing - that was the worst.

I used NumPy for easier manipulation (arithmetics mainly) of 2D array.

Here's the main algorithm:
A scanner visits its own beacon. Concurrently, another scanner visits its own beacon.
If these 2 scanners happen to visit the same (overlapping) beacon, that means these 2 scanners share an overlapping region of beacons.

What helps is to create "verbs" for what a scanner can do:
* it can move to its own beacon
* it can find how many beacons are overlapping with another scanner
* it can align with another scanner (zeroing itself etc.)

Also, I created a "hash" for every beacon, taking only the absolute (x,y,z) of the coordinates and ignoring the order of the x, y and z's 😱 (I mean it worked didn't it).

The rest of the algorithm is just zeroing of the coordinates and making sure that they are in the right columns, which is the part that I had a lot of bugs with.

Time complexity: *O(sb²)*, where *s* is the number of scanners and *b* is the number of beacons per scanner.
