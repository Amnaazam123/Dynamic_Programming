
# =============================================================================================================================
# Problem statement:
# Say that you are traveler on 2D grid. You begin in the top-left corner and your goal is to move towards bottom-right corner.
# You may only move down and right. In how many ways you can travel to the goal on the grid with dimensions m*n?
# Write a function `gridTraveler(m,n)` that calculates this.
# =============================================================================================================================


def gridTraveler(m,n):
    if(m==0 or n==0):
        return 0
    if(m==1 and n==1):
        return 1
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)

