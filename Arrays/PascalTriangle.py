# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows) :
            current_row = [1] * (i+1)
            for j in range(i + 1):
                if i > 1 and (j > 0 and j < i) :
                    current_row[j] = result[i-1][j-1] + result[i - 1][j]
            result.append(current_row)    

        return result    