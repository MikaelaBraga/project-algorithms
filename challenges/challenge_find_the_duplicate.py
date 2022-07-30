def find_duplicate(nums):
    nums.sort()
    
    counter = 0
    num = nums[0]
    
    for i in nums:
        curr_freq = nums.count(i)
        
        if curr_freq > counter:
            counter = curr_freq
            num = i
        
    return num
