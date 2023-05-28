batch1 = [1,2,3,4]
batch2 = [5,6,7,8,9]

merged_list = batch1 + batch2
merged_list.sort()
n = len(merged_list)
if n % 2 == 0:
    median = (merged_list[n//2-1] + merged_list[n//2])/2
else:
    median = merged_list[n//2]
print(median)