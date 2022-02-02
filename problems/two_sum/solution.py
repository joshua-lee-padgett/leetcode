####################
###
### Solution to two-sum problem under the assumption that the solution exists.
###
####################

##########
###
### O(n^2) solution using brute force
###
##########

# The following solution works by checking all possible combinations via brute force.
# Commented out --- only here for notes.

#class Solution:
#   def twoSum(self, nums: List[int], target: int) -> List[int]:
#        for i in range(len(nums)-1):
#            for j in range(i,len(nums)):
#                if nums[i] + nums[j] == target:
#                    return [i,j]

##########
###
### O(n) solution using hash map
###
##########

# self - allows function to access attributes and methods of the class
# -> - function annotation to specify output is a list of integers

class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {} # initialize empty hash map
       for i, value in enumerate(nums): # creates pair of iterables
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]] # if the reaminder is in the hash map
                                           # return the desired pair
            
           seen[value] = i # if the remainder is not in the hash map, update has map