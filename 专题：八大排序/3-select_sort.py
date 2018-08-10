#简单选择排序：选择最小值与未排序首个元素交换 
class Solution(object):
	def select_sort(self, L):
		m=0
		j=0
		while m<len(L):
			tmp=L[m]+1    #每次找最小值要重新初始化最小值
			for i in range(m,len(L)):
				if(L[i]<tmp):
					tmp=L[i]
					j=i
			L[m],L[j]=L[j],L[m]
			m=m+1
		return L

myList = [1,4,2,7,9,8,3,6]
print('init:',myList)
mySolu=Solution()
new_sorted=mySolu.select_sort(myList)
print(new_sorted)
