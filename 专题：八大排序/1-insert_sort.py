
#希尔方法下的直接插入法（通过step=1的交换）交换插入法[默认]
class Solution(object):
	def shell_sort(self, L):
		for i in range(1,len(L)):
			j=i
			while j>=1 and L[j]<L[j-1]:
				L[j],L[j-1]=L[j-1],L[j]
				j=j-1
		return L

myList = [6,4,2,7,9,8,3,1]
print('init:',myList)
mySolu=Solution()
new_sorted=mySolu.shell_sort(myList)
print(new_sorted)


#下面是移动插入法
'''
class Solution(object):
	def insert_sort(self, list0):
		for i in range(len(list0)):
			if(i==0):pass
			else:
				for j in range(i):
					if(list0[i]<list0[(j)]):
						tmp=list0(i)
						for m in range(i-1,j-1,-1):
							list0[m+1]=list0[m]
						list0[j]=tmp
						break
		return list0

myList = [49,38,65,97,76,13,27,49]
mySolu=Solution()
new_sorted=mySolu.insert_sort(myList)
print(new_sorted)
'''