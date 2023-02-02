## Problem1 
# Combination Sum (https://leetcode.com/problems/combination-sum/)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        print(candidates, target)
        res = []
        def backtrack(remaining, comb, start_index):
            if remaining==0:
                res.append(list(comb))
                return
            if remaining<0:
                return
            for i in range(start_index, len(candidates)):
                comb.append(candidates[i])
                # print("paina comb ", comb)
                # print("remaing", remaining - candidates[i])
                backtrack(remaining - candidates[i], comb, i)
                comb.pop()
                # print("kinda comb ", comb)
        
        backtrack(target, [], 0)
        return res