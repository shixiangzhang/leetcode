
def stringCompression(chars):
    chars = list(chars) # string is immutable, please check if input is string or list
    head = 0
    tail = 0
    length = len(chars)
    nth = 0
    for tail,ele in enumerate(chars):
        if (tail + 1) == length or ele != chars[tail + 1]: #check length should be the left of or, since tail+1 may out of list index
            chars[nth] = ele
            nth += 1
            if tail > head:
                for number in str(tail-head+1):
                    chars[nth] = number
                    nth +=1
            head = tail + 1
    return "".join(chars[0:nth])




if __name__=='__main__':
    #fptr = open('D:\programming\Python\\training\leetcode\\443stringCompression\output','w')
    #chars = input().strip()
    chars = 'aaabaaaaccaaaaba'
    res = stringCompression(chars)
    print(res)
    #fptr.write('\n'.join(map(str,res)))
    #fptr.write('\n')
    #fptr.close()