#基数排序 O(kn)

import random
def radixSort():
    A=[random.randint(1,9999) for i in range(10)]  
    for k in range(4):  #4轮排序      
        s=[[] for i in range(10)]
        for i in A:
            s[int(i/(10**k))%10].append(i)
        A=[a for b in s for a in b]
    return A

a = radixSort()
print(a)
