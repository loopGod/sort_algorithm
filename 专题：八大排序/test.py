#插入
def insert(li):
	lent=len(li)
	for i in range(1,lent):
		j=i
		while j>=1 and li[j]<li[j-1]:
			li[j],li[j-1]=li[j-1],li[j]
			j-=1
	return li

li=[4,5,1,2,8,4,5,6,2,1,8,4,9]
res=insert(li)
print(li)

#shell
def shell(li):
	lent=len(li)
	step=int(lent/2)
	while step>=1:
		for i in range(step,lent):
			j=i
			while j>=step and li[j]<li[j-step]:
				li[j],li[j-step]=li[j-step],li[j]
				j-=step
		step=int(step/2)
	return li

li=[4,5,1,2,8,4,5,6,2,1,8,4,9]
res=insert(li)
print(li)

#简单选择
def select(li):
	i=0
	lent=len(li)
	for j in range(0,lent-1):
		tmp=li[j]
		for m in range(j,lent-1):
			if li[m+1]<tmp:
				tmp=li[m+1]
				index=m+1
		li[index],li[i]=li[i],li[index]
		i+=1
	return li
li=[4,5,1,2,8,4,5,6,2,1,8,4,9]
res=select(li)
print(li)

#堆排序

#冒泡
def bubble(li):
	for i in range(1,len(li)):
		for j in range(len(li)-i):
			if li[j]>li[j+1]:
				li[j],li[j+1]=li[j+1],li[j]
	return li
li=[4,5,1,2,8,4,5,6,2,1,8,4,0]
res=bubble(li)
print(li)

#快速
def mid_sort(li):
	tmp=li[-1]
	i=-1
	for j in range(len(li)-1):
		if li[j]<tmp:
			i+=1
			li[j],li[i]=li[i],li[j]
	li[-1],li[i+1]=li[i+1],li[-1]
	return i+1

def fast_sort(li):
	if len(li)>1:
		index=mid_sort(li)
		li[0:index]=fast_sort(li[0:index])
		li[index+1:]=fast_sort(li[index+1:])
	return li
li=[4,5,1,2,8,4,5,6,2,1,8,4,0]
res=fast_sort(li)
print(li)

#归并
def merge(A,B):
	li=[]
	i=j=0
	while i<len(A) and j<len(B):
		if A[i]<=B[j]:
			li.append(A[i])
			i+=1
		else :
			li.append(B[j])
			j+=1
	if i==len(A):
		while j<len(B):
			li.append(B[j])
			j+=1
	else:
		while i<len(A):
			li.append(A[i])
			i+=1
	return li
def merge_sort(li):
	if len(li)<2:
		return li
	miiddle=int(len(li)/2)
	left=merge_sort(li[:miiddle])
	right=merge_sort(li[miiddle:])
	return merge(left,right)
li=[4,5,1,2,8,4,5,6,2,1,8,4,0]
res=merge_sort(li)
print(res)

#基数
def base(li,k):
	for i in range(k):
		bar=[[] for b in range(10)]
		for a in li:
			bar[int(a/(10**k))%10].append(a)
		li=[a for b in bar for a in b]
	return li
li=[4,5,1,2,8,4,5,6,2,1,8,4,0]
res=base(li,2)
print(res)
