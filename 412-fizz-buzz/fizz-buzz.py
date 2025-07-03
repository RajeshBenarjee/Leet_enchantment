class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i) for i in range(1, n + 1)]
        
        for i in range(2, n, 3): 
            if (i + 1) % 5 != 0:
                res[i] = 'Fizz'
        
        for i in range(4, n, 5):  
            if (i + 1) % 3 != 0:
                res[i] = 'Buzz'
        
        for i in range(14, n, 15): 
            res[i] = 'FizzBuzz'
        
        return res
