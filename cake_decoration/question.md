On a nice cozy morning of the new year, chef stepped out of his house to reach his workplace i.e. the famous Cheffy Bakery. On reaching, he found out that the head chef has ordered a new machine for easing the process of making cakes. 

In this new machine, there's a conveyor belt with places for exactly $N$ cakes (numbered $1$ to $N$). Initially, when the all the $N$ cakes are placed on the belt, there's no decoration on them. The machine puts decoration on a cake to make it look beautiful. The $i^{th}$ cake can contain a maximum of $D_{i}$ decorations.

The head chef has set some rules that chef has to follow: 

Choose a random number $C$ (where $1 ≤ C ≤ N$) and apply a decoration using machine on each of the cakes numbered $1, 2, 3,...., C$. The random number can be chosen any number of times.

The chef is told that he has to put as many decorations as possible on the cakes. The chef is not allowed to exceed the maximum number of decorations on a cake. Now your task is to help the chef calculate the maximum number of decorations that can be put on the cakes.

---
***Input***

The first line of the input contains a single integer $T$ denoting the number of test cases.

The first line of each test case contains a single integer $N$ denoting the number of cakes placed in the conveyor belt.

The second line contains $N$ space-separated integers $D_{1}$, $D_{2}$, … , $D_{N}$ denoting maximum decoration on $i^{th}$ cake.

---
***Output***

For each test case, print a single line containing one integer - the maximum number of decorations that can be put on the cakes.

---
***Constraints***

$1≤T≤100$

$1≤N≤10^{5}$

$1≤D_{i}≤10^{5}$ for each valid $i$

---
***Sample Input***

    2

    2

    7 1

    3

    8 7 4

---

***Sample Output***

    8

    19

---

***Explanation***

**For case 1** of the 2 test cases, choose (random integer) $C = 1$ six times, choose $C=2$ once.
