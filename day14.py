# count total substring with k distict character

s="pqpqs"
k=2
n=len(s)

def count_substr(s,k):
    total=0

    for i in range (n):
        char_count=set()
        for j in range (i,n):
            char_count.add(s[j])
            if len(char_count)==k:
                total+=1
            elif len(char_count)>k:
                break
    return total

print(count_substr(s,k))