class Solution(object):
    def plusOne(self, digits):
        number=0
        def decrypt(digits):
            num=0
            for i in digits:
                num=num*10+i
            return num
        number=decrypt(digits)+1
        def encrypt(number):
            n_list=[]
            while(number!=0):
                t=number%10
                number=number//10
                n_list.insert(0,t)
            return(n_list)
        return(encrypt(number))