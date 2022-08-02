'''
1)N denoting the size of array
2)A contains N space-separated integers denoting elements of array
3)b contains the no of queries
4)queries contains the arrays bu denoting[x,l,r]
    x value should be added to the array with l to range. Ex:A[l:r] should add the value x
5)After finishing with the queries than select the two min elements in a array, remove them from the array and append
their sum to the array.
Repeat this process until array consist of a single element.
                                        Thank you:)
'''





N=5
A=[1,4,3,2,4]
b=2
queries=[[5,1,2],[-5,1,3],[8,1,4]]
length=len(queries)
for i in range(length):
    q1=queries[i][1]
    q2=queries[i][2]
    for j in range(q2):
        A[j]+=queries[i][0]
    print(A)
while len(A)>1:
    sort_it=sorted(A)
    c=sort_it[0]
    d=sort_it[1]
    A.remove(c)
    A.remove(d)
    A.append(c+d)
print(A)
