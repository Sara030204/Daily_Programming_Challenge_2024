
# rearranged the array which only contains 0's , 1's , 2's in increasing order  in linear time
arr=[0,2,1,0,0,2,1,1,2,0]
n=len(arr)

i=1

for i in range(0,n):
    for j in range (i,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print(arr)