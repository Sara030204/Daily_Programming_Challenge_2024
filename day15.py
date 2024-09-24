#0find the longest substring without repeating character 

s="abcdefgh"

def longest_substring(s):
    n = len(s)
    seen = set()
    longest_substring = ""
    i = 0
    j = 0

    while i < n and j < n:
        if s[j] not in seen:
            seen.add(s[j])
            j += 1
            if j - i > len(longest_substring):
                longest_substring =s[i:j]
        else:
            seen.remove(s[i])
            i+=1

    return longest_substring

print(longest_substring(s))
