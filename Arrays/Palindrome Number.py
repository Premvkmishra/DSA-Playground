def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    og = str(x)
    
    reversed_str = og[::-1]
    
    return og == reversed_str