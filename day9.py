# #find a longest common prefix 

strings=["apple", "ape", "april"]

def find_common_prefix(strings):
    common_prefix=""

    string=strings[0]
            
    for i in range(len(strings[0]),0,-1):
        substr=string[:i]
        result=all(s.startswith(substr) for s in strings)
        if result==True :
            common_prefix=substr
            break
    return common_prefix
    
print(find_common_prefix(strings))
