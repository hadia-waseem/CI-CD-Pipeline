from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) #[1,1,1,1]
        prefix = 1
        for i in range(len(nums)): #
            res[i] = prefix #[1,1,2,6]
            prefix *= nums[i] #prefix = 6*4=24
        postfix = 1
        for i in range(len(nums) -1,-1,-1):#[]
            res[i] *= postfix  # [24,12,8,6]
            postfix *= nums[i] #postfix =24*1
        return res

        
def main():
    nums = [1, 2, 3, 4]
    solution = Solution()
    result = solution.productExceptSelf(nums)
    print("Result:", result)

if __name__ == "__main__":
    main()