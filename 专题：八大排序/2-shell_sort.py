
class Solution(object):
	def shell_sort(self, L):
	    step0 = int(len(L)/2)
	    while step0 > 0:
	        for j in range(step0,len(L)):            #在索引为step到len（L）上，比较L[i]和L[i-step]的大小
	            i=j
	            while(i >= step0 and L[i] < L[i-step0]):      #这里可以调整step从小到大或者从大到小排列
	                L[i],L[i-step0] = L[i-step0],L[i]
	                i -= step0
	        step0=int(step0/2)
	    return L

myList = [1,4,2,7,9,8,3,6]
print('init:',myList)
mySolu=Solution()
new_sorted=mySolu.shell_sort(myList)
print(new_sorted)


'''
#希尔方法下的直接插入法（通过step=1的交换）
class Solution(object):
	def shell_sort(self, L):
		for i in range(1,len(L)):
			while i>=1 and L[i]<L[i-1]:
				L[i],L[i-1]=L[i-1],L[i]
				i=i-1
		return L

myList = [1,4,2,7,9,8,3,6]
print('init:',myList)
mySolu=Solution()
new_sorted=mySolu.shell_sort(myList)
print(new_sorted)
'''