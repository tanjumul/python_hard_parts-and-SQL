class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       
        nums.sort()

        for i in range(1,len(nums)): 
            if nums[i] == nums[i-1]:
                return True
        return False


#i took a day off planed a little and thought what i should be doing in 2 next month , building and breaking and reshaping my 
#lost career ! Backend it is.. 






"""Nothing here fancy : 
here the nums is as a list now : 
i don't know how the numbers are formed inside the list , 
i will sort it first of the messy like numbers can be alligned like Example : 
Before : nums[12,1,44,2,6,4,3,0,6]
After : nums[0,1,2,3,4,6,6,12,44]

now i , looped form 1 to length of the array , some time without 1 it give your a true result which is wrong. 
after that you do a condition check weather the index of nums is matching with it's previous index , if matching `return True not in 'true' form ` without it can give you error. thta's it break the loop and add your next return."""