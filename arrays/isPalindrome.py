def isPalindrome(x):
    arr = []
    while x > 0:
        remainder = x % 10
        x = x // 10
        arr.append(remainder)
    
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True

x = 18781
print(isPalindrome(x))