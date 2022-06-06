def checkifPalindromeornot(word):
    return word == word[::-1]
 
 
word = input("Enter the word:")
ans = checkifPalindromeornot(word)
 
if ans:
    print("Yes")
else:
    print("No")
