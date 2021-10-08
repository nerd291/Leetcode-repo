class Solution:
    def twoSum(nums: list[int],target):
        for x in range (0,len(nums)):
            for y in range (0,len(nums)):
                z = 0
                z = nums[x]+nums[y]
                if (z==target):
                    print("[{},{}]".format(x,y))
                    exit()
                else:
                    continue
                z=0

    print(twoSum([3,3],6))