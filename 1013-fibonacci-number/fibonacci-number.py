class Solution:
    def fib(self, n: int) -> int:
        fib = [0,1]

        # From the given numbers we can build up to any number of fibonacci
        for i in range(2, n+1):
            # Fibonacci is the result of the addition of the two previous numbers
            # Append such numbers to array until array has reached target number
            fib.append(fib[i-1] + fib[i-2])
        
        # Return the target number stored in our array
        return fib[n]