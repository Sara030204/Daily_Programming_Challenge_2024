
#find the leader elements.

arr=[7, 10, 4, 10, 6, 5, 2]
leaders=[]
  
max_element=arr[-1]
leaders.append(max_element)

for i in range (len(arr)-2,-1,-1):
    if arr[i]>max_element:
        leaders.append(arr[i])
        max_element=arr[i]
leaders.reverse()
print(leaders)