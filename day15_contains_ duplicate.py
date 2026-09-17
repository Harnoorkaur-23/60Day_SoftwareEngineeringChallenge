class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Create an empty set to keep track of numbers we have already seen
        seen = set()
        
        # Loop through each number in the input list
        for num in nums:
            # If the number is already in our set, we found a duplicate!
            if num in seen:
                return True
            
            # If it's a new number, add it to our set and keep moving
            seen.add(num)
            
        # If the loop finishes and no duplicates were found, return False
        return False
