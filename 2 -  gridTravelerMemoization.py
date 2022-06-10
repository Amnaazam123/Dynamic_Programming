
# =============================================================================================================================
# Problem statement:
# Say that you are traveler on 2D grid. You begin in the top-left corner and your goal is to move towards bottom-right corner.
# You may only move down and right. In how many ways you can travel to the goal on the grid with dimensions m*n?
# Write a function `gridTraveler(m,n)` that calculates this.
# =============================================================================================================================


#time complexity(2^(m+n))
def gridTraveler(m,n):
    if(m==0 or n==0):
        return 0
    if(m==1 and n==1):
        return 1
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)


# =============================================================================
# How this above solution is working?
# Make a tree where each node has two values and two childs,
# one showing downward grid and one showing right grid until you reach base cases.
# =============================================================================


#memoization to reuse repetitive steps
#time complexity(m*n)
def gridTraveler(m,n,memo={}):
    key = str(m) + "," + str(n)
    if key in memo:
        return memo[key]
    if(m==0 or n==0):
        return 0
    if(m==1 and n==1):
        return 1
    memo[key] = gridTraveler(m-1, n,memo) + gridTraveler(m, n-1,memo)
    return memo[key]

