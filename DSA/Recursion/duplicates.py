class solution:
    def removeDuplicates(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
res = solution()
print(res.removeDuplicates([1,2,3]))
