nums=[1,1,2,2,2,3]
result={}
for n in nums:
    if n in result:
        result[n].append(n)
    else:
        result[n]=[n]
print(result)