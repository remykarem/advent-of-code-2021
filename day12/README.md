# Day 12

We define the problem as such:

* if you visit the end, you 'win', i.e. you are rewarded with 1 point
* if you try to visit a cave that you've visited before, you 'die', i.e. you are rewarded with 0 points
* otherwise just keep exploring other caves until you win or lose

so that we can define it recursively. Here, a 1-point indicates a unique path.

There is also a data structure called `node2children` that keeps track of a node's possible connections.

Solution does not include memoisation.
