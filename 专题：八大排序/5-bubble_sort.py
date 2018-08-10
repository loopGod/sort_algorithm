#冒泡排序

#coding: utf-8  
class Solution(object):
    def bubble_sort(self,L):
        length=len(L)
        in_len=length
        for j in range(length-1):
            in_len=length-j
            for i in range(in_len-1):
                if(L[i]>L[i+1]):
                    L[i],L[i+1]=L[i+1],L[i]
        return L

mySolu=Solution()
L=[5,8,4,9,6,4,7,5,2,1,3,6,5,8]
new_list=mySolu.bubble_sort(L)
print(new_list)
        
