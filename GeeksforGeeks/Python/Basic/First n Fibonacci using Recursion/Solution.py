class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        if n==1:
            return [0]
        elif n==2:
            return [0,1]
        arr=[0,1]
        for i in range(2,n):
            arr.append(arr[-1]+arr[-2])
        return arr
        