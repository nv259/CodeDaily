class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def binary_search(arr, key):
            low, high = 0, len(arr) - 1
            ans = len(arr)

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] >= key:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1 
            
            return ans

        ans = []
        for spell in spells:
            min_potion_strength = success / spell

            left_most_satisfied_potion_idx = binary_search(potions, min_potion_strength)
            ans.append(len(potions) - left_most_satisfied_potion_idx)
        
        return ans