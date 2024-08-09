import os,json
os.system("cls")
class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        for i in range(len(arr) - 2 - (1 if len(arr) > 3 else 0)):
            if sum(arr[i:i + 3]) % 2:
                return True
        return False


print(Solution().threeConsecutiveOdds([2, 6, 4, 1]))
print(Solution().threeConsecutiveOdds([1, 1, 1]))
print(Solution().threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
