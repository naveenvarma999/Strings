# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
def ispalindrome():

    s = input("Enter the text: ")
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()
    if cleaned == cleaned[::-1]:
        return True
    else:
        return False
result = ispalindrome()
print(result)