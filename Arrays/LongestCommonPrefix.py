# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs : 
            return "Please enter a valid array"
        prefix = strs[0]
         
        for i in range(1,len(strs)):

            current_str = strs[i]
            j = 0 
            while j < len(prefix) and j < len(current_str) and prefix[j] == current_str[j]:
                j +=1
                
            prefix = prefix[0:j]    

        return  prefix    