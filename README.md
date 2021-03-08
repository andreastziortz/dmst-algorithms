# dmst-algorithms-course
Through these three assignments , i was able to create small python scripts , using well known algorithms that play a major role as subroutines or even as essential functions in many different programmes.

1 assignment
During the first assignment , the problem was ,given a constant number of squares (n), to try calculate the number of constant polyominoes that could be formed for any number of squares that would be given.That means that number n (number of squares) is a random number.

2 assignment
Given a network, which is represented by a set of nodes, the aim was to find the nodes that influence most of all the network.We used to methods for this task.

1)We consider as most infectious the nodes that were marked by the highest number of connected nodes to themselves(grade of node).
  We subtract the node with highest score nd adjust the grade of nodes that were connected with it.We recalculate the grade for every node and follow the same procedure until the intended nuber of nodes have been subtracted.
  
2)We examine the nodes that has the most major impact to the network,according to this formula:
CI(i,r)=(Ki−1)∑j∈ϑBall(i,r)(Kj−1)
where,
i: is the node that we are interested to calculate and Ki is the number of connections of node i.

Ball(i,r):the set of nodes where shortest path from has length less or equal of constant r.So these are the nodes j that incorporate in a circle(i,r),that means a circle with centre the node i and radius equals to r.

ϑBall(i,r) : set of nodes that shortest path from i equals to r.Explicitly, these nodes are on the circumference of the circle (i,r).In 3 dimensional space are the nodes thatare on the surface of a sphere (i,r)

Calculating total inluence of every node,we subtract this with the highest score adn adjust the influence of nodes that exist in Ball(i,r),according to the norm
We repeat the same process for as nodes we need.


3 assignment
Among the rules that were implmented during the pandemic was social distancing rules.That raises the question , if we have a certain space , how many people are able to allocate appropriately and in which structure without violating distance's rules.If we represent every person with a circle,the goal is to induce the highest number of circles with a certain radius inside the space that is drawn by a geometrical shape.So,given a space and a minimum distance required ,we can find how many people could fit in.
