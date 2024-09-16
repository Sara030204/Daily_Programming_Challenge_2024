# REverse a string word by word 

input=" the sky is  blue "

def reverse(input):

    word=input.split()
    word_array=word[::-1]

    reversed_string=" ".join(word_array)
    return reversed_string

print(reverse(input))