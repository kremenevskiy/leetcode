from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = [str(i) for i in range(1, n+1)]
        for i in range(2, n):
            by_3 = (i + 1) % 3 == 0
            by_5 = (i + 1) % 5 == 0
            if by_3 and by_5:
                arr[i] = "FizzBuzz"
            elif by_3:
                arr[i] = "Fizz"
            elif by_5:
                arr[i] = "Buzz"
        print(arr)
        return arr
            


n = 3
ans = ["1","2","Fizz"]
assert Solution().fizzBuzz(n) == ans

n = 5
ans = ["1","2","Fizz","4","Buzz"]
assert Solution().fizzBuzz(n) == ans

n = 15
ans = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
assert Solution().fizzBuzz(n) == ans

