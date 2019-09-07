
def twoSum(nums,target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dictCheck = {}
    for i,singNum in enumerate(nums):
        numNeed = target - singNum
        if numNeed in dictCheck: #use numNeed in dictCheck.keys() takes 650ms time instead of 32ms.
            return ([dictCheck[numNeed],i])
        else:
            dictCheck[singNum] = i
    return []



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