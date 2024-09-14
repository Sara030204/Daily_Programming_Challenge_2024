#find the subarray whose sum is up to 0 and subarray must be continueous 

arr=[0, 0, 0]

subarray=[]

def find_subarray(arr):
    n=len(arr)
    
    for i in range (n):
        sum=0
        for j in range (i,n):
            sum+=arr[j]
            if sum==0:
                subarray.append((i,j))

    return subarray

print(find_subarray(arr))
