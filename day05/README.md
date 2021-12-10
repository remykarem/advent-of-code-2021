**2D**

Initially wanted to use a 2D array to represent the data structure but thank goodness I didn't. Space *O(mn)* where *m* is the max *x* and *n* is the max *y*.

**2D sparse**

Later realised that this is possibly sparse, so we use a count dictionary `Map<Point, Count>` instead.
