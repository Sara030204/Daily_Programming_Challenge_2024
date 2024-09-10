#find the mising element from the series 

arr=[1,2,3,4,5,6]
n=len(arr)+1

sum_of_n_numbers=n * (n + 1) // 2  #using formula
array_sum=sum(arr)

missing_element=sum_of_n_numbers -array_sum
print("missing_element :",missing_element)