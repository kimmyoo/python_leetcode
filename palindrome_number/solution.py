""" determine if a number is a palindrome
palindrome: a number can be mirrored in the middle
e.g. 123321 is a palindrome; 12321 is a palindrome """
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        num_digit = 0
        y = x
        while y != 0:
            y //= 10 #notice the difference between y/10 and y//10
            num_digit += 1

        if num_digit <= 1:
            print("single digit number is a palindrome.")
            return True
        # Reverse the right half
        i = 0
        t = 0
        # if num_digit is odd, x needs extra floor division by 10
        # in the following while loop
        if num_digit % 2 == 0:
            counter = num_digit - 1
        else:
            counter = num_digit
        # e.g. x = 121    num_digit = 3   range of i: 0 to 1
        # i = 0; t = 0 * 10 + 1 = 1
        # x = 12; i increments to 1
        # i = 1; t = 1 * 10 + 2 = 12
        # x = 1, i increments to 2
        # while loop breaks
        while i <= counter // 2:
            #print (x)
            t = t * 10 + x % 10
            x = x // 10
            i += 1
        print ("this is current x:", x)
        print ("this is current t:", t)
        # Remove the middle digit if num_digit is odd
        if num_digit % 2 == 1:
            t //= 10
        print ("if odd number of digits, t is trimmed to:", t)
        if t == x:
            return True
        else:
            return False

s = Solution()
print (s.isPalindrome(1221))
print (s.isPalindrome(0))
print (s.isPalindrome(-121))
