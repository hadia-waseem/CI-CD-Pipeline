class Solution:
    def maxDepth(self, s: str) -> int:
        currdepth = 0
        maxD = currdepth
        
        for i in s:
            if i == '(':
                currdepth += 1
                maxD = max(maxD, currdepth)
            elif i == ')':
                currdepth -= 1
        return maxD

if __name__ == "__main__":
    solution = Solution()
    test_string = "(1+(2*3)+((8)/4))+1"
    print("Maximum depth of", test_string, ":", solution.maxDepth(test_string))
    
    test_string = "((())()(()))"
    print("Maximum depth of", test_string, ":", solution.maxDepth(test_string))
