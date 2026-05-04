nums=[2,4,3,5,7,8]
target=7
for i in nums:
    for j in nums:
        if i+j==target and i<j:
            print(i,j)