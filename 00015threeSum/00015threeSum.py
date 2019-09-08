
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    length = len(nums)
    for i in range(length-2):
        if(nums[i]>0):break
        if (i>0) and (nums[i]==nums[i-1]):continue
        l = i+1
        r = length-1
        while l<r:
            total = nums[i]+nums[l]+nums[r]
            if total<0:
                l += 1
            elif total>0:
                r -= 1
            else:
                res.append([nums[i],nums[l],nums[r]])
                while (l<r) and (nums[l]==nums[l+1]): #can't use &, difference between & "and" is & will calculate both left and right side, use [0,0,0] to test
                    l += 1
                while (l<r) and (nums[r]==nums[r-1]):
                    r -= 1
                l += 1
                r -= 1
    return res

if __name__=='__main__':
    #fptr = open('D:\programming\Python\\training\leetcode\\00443stringCompression\output','w')
    #chars = input().strip()
    nums = [0,0,0]
    res = threeSum(nums)
    print(res)
    #fptr.write('\n'.join(map(str,res)))
    #fptr.write('\n')
    #fptr.close()