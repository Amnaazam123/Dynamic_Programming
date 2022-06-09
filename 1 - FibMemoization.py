#ctrl+4 to comment multiple line in python.
#ctrl+5 to uncomment multiple lines in python


# =============================================================================
# Problem Statement: 
# Write a function `fib(n)` that takes in a number as an argument. 
# The function should return the nth number of Fibonacci Sequence.
# 
# =============================================================================


#using recursion, It is obvious
#time complexity(2^n)
def fib(n):
    if(n<=2):
        return 1
    return fib(n-1)+fib(n-2)


print(fib(30))           


#What was problem in recursion solution
#Ans: The solution has correctness but lacks efficiency.
#How To make your solution EFFICIENT?
#Ans: MEMOIZATION(store some duplicate sub-problems so that i can just get those results later on.)


# Memoization
# Time complexity(O(n))
# =============================================================================
# 
# How it is working?
# To understand this code:
# - Make fibo tree which will call two recursive calls n-1 and n-2 at each node.
# - After that from leaf nodes, start to return values and store the results in memo dictionary as well.
# - check for condition if n in memo retun memo[n] and update your dictionary.
# - memo is nothing but dictionary which will store "n" as key and fibValue[n] as value. 
# 
# 
# =============================================================================

def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if(n<=2):
        return 1
    memo[n] = fib(n-1,memo)+fib(n-2,memo)     #why passing memo parameter? so that we can check if condition for updated memo each time.
    return memo[n]


print(fib(50))


    
