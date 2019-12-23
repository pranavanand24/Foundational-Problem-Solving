def  largest(arr,n) :
    #initialize max element
    max= arr[0]
    #traverse array from second and compare every with current max
    for i in range(1 , n):
           if  arr[ i ] > max :
                 max = arr[i]
    return max
    
#driver code
arr = [ 10, 95, 324, 71]
n = len(arr)
ans =  largest(arr, n)
print (" the largest element in a array ", ans )
               