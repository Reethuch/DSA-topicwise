# TC : O(log n)
# SC : O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        while left < right:
            mid = left + (right - left)//2
            print(x, mid, left, right)
            if x <= arr[mid]:
                right = mid
            elif x >= arr[mid + k]:
                left = mid + 1
            elif x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]
#         low = 0
#         found = 0
#         high = len(arr) - 1
#         while low <= high:
#             mid = low + (high - low)//2
#             if arr[mid]==x:
#                 found = 1
#                 break
#             elif arr[mid] <= x <= arr[mid+1]:
#                 break
#             elif arr[mid] > x:
#                 high = mid - 1
#             elif arr[mid] < x:
#                 low = mid + 1
#         print(mid, arr[mid],found)
#         return self.find_nearest(arr, mid, k, found, x)
    
#     def find_nearest(arr, ind, k, found, x):
#         res = []
#         if found:
#             res.append(x)
#             k -= 1
#             while k:
            
        
        
                
        