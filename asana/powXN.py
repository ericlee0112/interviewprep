class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Step 1: Handle base case
        if n == 0:
            return 1
        
        # Step 2: Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
    # Step 3: Recursive Exponentiation by Squaring
    def power(self, x, n):
        if n == 0:
            return 1
        half = self.power(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x