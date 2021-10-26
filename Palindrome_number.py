import math
class Solution(object):
    def isPalindrome(self,x):

        if(x<0 or x%10==0):
            return False
            
        revertedNumber=0

        while(x>revertedNumber):
            revertedNumber=revertedNumber*10+x%10
            x/=10

        return (x==revertedNumber or x==revertedNumber/10)


        # my code:    
        # if(x<0 or x%10==0):
        #     print(False)
        #     return
        # stringX=str(x)
        # count=0

        # for x in range(len(stringX)):
        #     if(stringX[count]!=stringX[len(stringX)-1-count]):
        #         x=False
        #     else:
        #         x=True
        #     if(count==math.ceil(len(stringX)/2)):
        #         break
        #     if(x==False):
        #         break
        #     count+=1

obj = Solution
obj.isPalindrome(obj,1221)