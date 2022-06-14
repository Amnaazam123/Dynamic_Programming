def howSum(targetSum,numbers):
    if(targetSum<0):
        return None
    if(targetSum==0):
        return []
    for num in numbers:
        r = howSum(targetSum-num, numbers)
        if(r!=None):
            return r.append(num)
    return None
         
print(howSum(7, [2,3,4,5]))










    
