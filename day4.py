
# merge two sorted array without extra space 

arr1 = [1]
arr2 = [2]

def merge_sorted_array(arr1,arr2):
    i=len(arr1) -1  
    j=0      
    
    while i >=0 and j<len(arr2):
        if arr1[i] > arr2[j]:
            # swap 
            arr1[i] , arr2[j] =arr2[j] , arr1[i]
        i =i-1
        j =j+1
    
    arr1.sort()
    arr2.sort()


merge_sorted_array(arr1, arr2)
print(arr1,'\n',arr2)  
