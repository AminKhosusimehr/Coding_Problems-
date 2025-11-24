# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
#
# You may return the answer in any order.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backTrack(path , options):
            if len(path) == k :
                result.append(path[:])
                return

            for i in range(len(options)) :
                path.append(options[i])
                new_options = options[i+1:]
                backTrack(path , new_options)
                path.pop()

        result = []
        numbers = list(range(1, n+1))
        backTrack([],numbers)
        return result