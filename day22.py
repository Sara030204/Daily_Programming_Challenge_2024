
# find first  element which exactly repeat k times 

arr=[6, 6, 6, 6, 7, 7, 8, 8, 8]

k=3
def search_element(arr,k):
    for i in arr:
        if arr.count(i)==k:
            return i 
        
    return -1

print(search_element(arr,k))