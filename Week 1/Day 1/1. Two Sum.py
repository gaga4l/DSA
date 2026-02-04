// Leetcode : https://leetcode.com/problems/two-sum/


// O(n^2)
for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
// O(n)
seen = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in seen:
                return [seen[x], i]
            seen[num] = i
                    