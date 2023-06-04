nums = [1, 7, 5, 2]

def two_sum(nums, target= 9):
    dico = {}
    for i in range(len(nums)):
        if target - nums[i] in dico:
            return [dico[target-nums[i]], i]
        else:
            dico[nums[i]] = i
            
print(two_sum(nums))
     