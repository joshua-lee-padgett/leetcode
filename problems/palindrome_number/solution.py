####################
###
### Solution to palindrome problem.
###
####################

##########
###
### Solution by converting number to string
###
##########

#class Solution:
#    def isPalindrome(self, x: int) -> bool:
#        
#        number = str(x) # convert to string
#        
#        return number[::-1] == number # compare string in both directions

##########
###
### Solution using a tmp variable
###
##########

#class Solution:
#    def isPalindrome(self, x: int) -> bool:
#        
#        palindromeCheck = 0
#        tmp = x
#        
#        while tmp > 0:
#            
#            palindromeCheck = palindromeCheck * 10 + tmp % 10
#            tmp = tmp // 10
#            
#        return x == palindromeCheck

##########
###
### O(n/2) solution (where n is the number of digits)
###
##########

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # if x is negative, it is not a palindrome
        # if x = 0, it is a palindrome
        # if x>0 and x%10=0, it is not a palindrome
        
        if x < 0 or ( x > 0 and x%10 == 0 ):
            return False
        
        palindromeCheck = 0 # placeholder
        
        while x > palindromeCheck:
            
            palindromeCheck = palindromeCheck * 10 + x % 10 # shift and add new digit
            x = x // 10 # remove old digit
            
        # if x is equal to palindromeCheck, it is a palindrome
        # if x has an odd number of digits, discard the middle digit before comparing
        
        return True if ( x == palindromeCheck or x == palindromeCheck // 10 ) else False