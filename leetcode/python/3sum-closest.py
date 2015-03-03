"""
https://oj.leetcode.com/problems/3sum-closest/

3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is 
closest to a given number, target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""


class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if not num:
            return 0
            
        length = len(num)
        if length <= 3:
            return sum(num)
            
        num.sort() 
        
        left = 0
        right = length - 1
        
        closest_sum = 0xFFFFFFFF

        while left < right - 1:
            two_sum = num[left] + num[right]
            
            delta = target - two_sum

            closest_idx = binary_search_closest(num, left + 1, right - 1, delta)
                                        
            new_sum = two_sum + num[closest_idx]

            if new_sum > target:
                right -= 1
            elif new_sum < target:
                left += 1
            else:
                return target
            
            if abs(target - closest_sum) > abs(target - new_sum):
                closest_sum = new_sum
            
        return closest_sum
        
        
def binary_search_closest(nums, left, right, value):
    while left < right:
        if value <= nums[left]:
            return left
        if value >= nums[right]:
            return right
            
        center = (left + right) / 2
        
        if value == nums[center]:
            return center
        elif value > nums[center]:
            left, right = center + 1, right - 1
        elif value < nums[center]:
            left, right = left + 1, center - 1
        else:
            # never here
            raise Exception("why r u here?")

    # return closest index
    if left != right and abs(nums[left] - value) > abs(nums[right] - value):
        return right

    return left
    
    
def test_main():
    import random
    
    sol = Solution()
       
    for i in xrange(10):
        numbers = random.sample(xrange(-10, 10), i)
        
        target = random.randint(0, 20)
        
        # numbers = [2, 16, 5, 0]
        # target = 19
        
        print("3sum closest in %s" % numbers)
        print(target, sol.threeSumClosest(numbers, target))
       
        
if __name__ == "__main__":
    test_main()
    
