#快速排序排序

#coding: utf-8  

def mid_sort(L,n,m):
	i=n-1
	for j in range(n,m):
		if(L[j]<=L[m]):
			i=i+1
			L[i],L[j]=L[j],L[i]
	L[i+1],L[m]=L[m],L[i+1]
	return i

def fast_sort(L,n,m):
	if(n<m):
		index=mid_sort(L, n, m)
		print(index)
		fast_sort(L, n, index)
		fast_sort(L,index+1,m)
	else:
		return  #这里递归不要用return返回值



L=[1,4,7,1,5,5,3,85,34,75,23,75,2,0]
new_list=fast_sort(L,0,len(L)-1)
print(L)

'''
def QuickSort(arr,n,m):
    if n<m:
        divIndex=Partition(arr,n,m)
        print(divIndex)
        QuickSort(arr,n,divIndex)       
        QuickSort(arr,divIndex+1,m)
    else:
        return
 
 
def Partition(arr,n,m):
    i=n-1
    for j in range(n,m):
        if arr[j]<=arr[m]:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[m]=arr[m],arr[i+1]
    return i
 
 
arr=[1,4,7,1,5,5,3,85,34,75,23,75,2,0]
 
print("initial array:\n",arr)
QuickSort(arr,0,len(arr)-1)
print("result array:\n",arr)    
'''