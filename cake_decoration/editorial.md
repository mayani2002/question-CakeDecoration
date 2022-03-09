## DIFFICULTY:

Easy-Medium

## PREREQUISITES:

Data Structure, Greedy.

## PROBLEM STATEMENT:

On a nice cozy morning of the new year, chef stepped out of his house to reach his workplace i.e. the famous Cheffy Bakery. On reaching, he found out that the head chef has ordered a new machine for easing the process of making cakes. 

The head chef gives a brief description of what the machine does as follows: 

In this new machine, there's a conveyor belt with places for exactly $N$ cakes (numbered $1$ to $N$). Initially, when the all the $N$ cakes are placed on the belt, there's no decoration on them. The machine puts decoration on a cake to make it look beautiful. The $i^{th}$ cake can contain a maximum of $D_{i}$ decorations.

The head chef has set some rules that chef has to follow: 

Choose a random number $C$ (where $1 ≤ C ≤ N$) and apply a decoration using machine on each of the cakes numbered $1, 2, 3,...., C$. The random number can be chosen any number of times.

The chef is told that he has to put as many decorations as possible on the cakes. The chef is not allowed to exceed the maximum number of decorations on a cake. Now your task is to help the chef calculate the maximum number of decorations that can be put on the cakes.

## EXPLANATION

According to the problem statement, for any $C^{th}$ random number, the cake from $1$ to $C$ will be decorated once. This gives the conclusion that if any $i^{th}$ cake has $X$ amount of decoration then $i+1^{th}$ cake will have decoration which is less that or equal to $X$. To achieve the total maximum decoration on all N cakes, each $i^{th}$ cake should have it's maximum decoration if the maximum decoration limit of previous cakes are greater than or equal to the maximum decoration limit of current cake. But if the maximum decoration limit of previous cakes is less than the maximum decoration limit of current cake then the cake should have decoration same as the $i-1^{th}$ cake. The sum of number of decorations on each cake will be the required answer.

**C++ Code (solution)**

    #include <iostream>
    #include <climits>
    using namespace std;

    int main() {
        int t;
        cin >> t;
        while (t--)
        {
            long long mini = INT_MAX;
            long long res = 0;
            long long n;
            cin >> n;
            for (long long i = 0; i < n; i++)
            {
                long long x;
                cin >> x;
                mini = min(x, mini);
                res += mini;
            }
            cout << res  << endl;
        }
        return 0;
    }

## TIME COMPLEXITY:

$O(N)$