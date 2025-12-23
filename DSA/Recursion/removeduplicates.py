class Solution:
    def removeduplicates(self, num):
        i = 1
        for j in range(1, len(num)):
            if num[j] != num[j-1]:
                num[i]= num[j]
                i += 1
        return i
    
# Create instance
sol = Solution()

# Test
nums = [1, 1, 2]
print(f"Input: {nums}")
k = sol.removeduplicates(nums)
print(f"Output: k={k}, Array={nums}")