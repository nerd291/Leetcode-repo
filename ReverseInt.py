class Solution:
    def reverse(x: int) -> int:
        nums = []
        count = int(10 ** ((x%10)-1))
        z=0
        c=0
        g=0
        for y in range (0, x%10):
            c = ((x-x%count)-z)
            z=(x-(x%count))
            count = count/10
            if z>0:
                nums.append(int(c/(count*10)))
        numstr=[]
        newnum = ""
        for x in range (0, len(nums)):
            numstr.append(str(nums[x]))
        g=len(numstr)-1
        for x in range (0,len(numstr)):
            newnum = newnum + numstr[g]
            g=g-1
        print(newnum)
    
    reverse(123)

    #input 123
    #output 321
    
    #input -123
    #output -321

    #input 120
    #output 21

    #input 0
    #output 0

    #things to work on for optomization:
    #turn nums[] into str nums[] and print 123 instead of 1 2 3
    #combine for y and for b into a statement that prints and also creates nums in reverse order
    #potentially remove z and c or combine them into something that can be used properly