# ===============================================================================================
# Problem statement:
# write a function `canSum(targetSum,numbers)` that takes in a targetSum and an array of numbers
# as arguments. This function should return boolean indicating whether or not it is possible
# to genrate targetSum from given numbers in array.
# ===============================================================================================

#using recursion
#time complexity(m^n)
def canSum(targetSum,numbers):
    if(targetSum == 0):
        return True 
    if(targetSum < 0):
        return False                                        
    for num in numbers:
        if(canSum(targetSum-num,numbers) == True):
            return True
            
print(canSum(7,[4,2,15,1]))



#using memoization
#time complexity(m^n)
def canSum(targetSum,numbers,memo={}):
    if(targetSum == 0):
        return True 
    if(targetSum < 0):
        return False  
    if(targetSum in memo):
        return memo[targetSum]                                      
    for num in numbers:
        
        if(canSum(targetSum-num,numbers,memo) == True):
            memo[targetSum]=True
            return True
    memo[targetSum]=False
    return False
  
  
  print(canSum(300,[4,3]))
            
