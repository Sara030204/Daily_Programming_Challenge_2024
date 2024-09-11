#find the duplicate element 

arr=[1,4,2,3,3]
n=len(arr)-1

sum_of_n_numbers=n * (n + 1) // 2  #using formula
array_sum=sum(arr)

duplicate_element=array_sum-sum_of_n_numbers
print("Duplicate element :",duplicate_element)