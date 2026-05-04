nums=[[1,2],[3,4],[5]]
flat=[]
for sublist in nums:
    for item in sublist:
        flat.append(item)
print(flat)