from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(path, remaining, depth=0):
            indent = "  " * depth
            print(f"{indent}↳ backtrack(path={path}, remaining={remaining})")
            
            if len(path) == len(nums):
                print(f"{indent}  ✅ جواب: {path}")
                result.append(path[:])
                return
            
            for i in range(len(remaining)):
                print(f"{indent}  i={i}: انتخاب {remaining[i]}")
                
                path.append(remaining[i])
                new_remaining = remaining[:i] + remaining[i+1:]
                
                print(f"{indent}    قبل از بازگشتی: path={path}, new_remaining={new_remaining}")
                backtrack(path, new_remaining, depth + 1)
                print(f"{indent}    بعد از بازگشتی: path={path}")
                
                removed = path.pop()
                print(f"{indent}    pop() → حذف {removed}, path={path}")
        
        backtrack([], nums)
        return result

# اجرا
sol = Solution()
print("شروع اجرا...")
result = sol.permute([1, 2, 3])
print(f"\n🎉 همه جایگشت‌ها: {result}")