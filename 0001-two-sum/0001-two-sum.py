class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the numbers and their indices
        num_map = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement that would sum up to the target
            complement = target - num
            
            # Check if the complement is in the dictionary
            if complement in num_map:
                # If found, return the indices of the complement and the current number
                return [num_map[complement], i]
            
            # Store the number and its index in the dictionary
            num_map[num] = i

# Example usage
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]
