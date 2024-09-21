# Longest Palindromic Substring

s="abaad"

n=len(s)
i=0
longest_palindrome=""

while i<n:
    if n-i<=len(longest_palindrome):
        break
    for j in range(n,i,-1):
        s_pal=s[i:j]
        reverse=s_pal[::-1]

        if s_pal ==reverse and len(s_pal)>len(longest_palindrome):
            longest_palindrome=s_pal
            break
    i=i+1

print("Longest Palindrome : ",longest_palindrome)
