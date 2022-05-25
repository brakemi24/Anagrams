# Check if a word is an anagrams
#find_anagrams("hello") --> False
#find_anagrams("racecar") --> True



def find_anagrams(word_1,word_2):
    # [assignment] Add your code here
    if sorted(word_1) == sorted(word_2):
        return True
    else:
        return False




word_1=input("Enter the first String: ")
word_2=input("Enter the second String: ")

if find_anagrams(word_1,word_2):
    print ('True')
else:
    print('False')    
