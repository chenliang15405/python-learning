
nums =[0,1,2,2,3,0,4,2]

nums2 = nums[:]

for i in range(len(nums)):
    if nums[i] == 2:
        nums.pop(i)
