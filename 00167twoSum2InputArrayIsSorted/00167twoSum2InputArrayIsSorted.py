"""
We could use Mathematical induction.  assume when you at x and y, then target = xTarget + yTarget, then xTarget >= x and yTarget<=y.
If x + y < target, x change to xnew which is x+1th, only case may missed is xnew, ytmp, ytmp > y,  but when y is ytmp, based on the rule, at that time, x is at xtmp, xtmp will move to xnew. No chance at x and y status
So it is proved.
"""

def twoSum(numbers,target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    xth = 0
    yth = len(numbers)-1
    curr = numbers[xth] + numbers[yth]
    while curr != target:
        if curr < target:
            xth = xth + 1
        else:
            yth = yth - 1
        curr = numbers[xth] + numbers[yth]
    return [xth+1,yth+1]


if __name__=='__main__':
    #fptr = open('D:\programming\Python\\training\leetcode\\00443stringCompression\output','w')
    #chars = input().strip()
    nums = [2, 7, 11, 15]
    target = 9
    res = twoSum(nums,target)
    print(res)
    #fptr.write('\n'.join(map(str,res)))
    #fptr.write('\n')
    #fptr.close()