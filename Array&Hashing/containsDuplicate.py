class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array,
        and return false if every element is distinct.
        """
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    # 🧪 Example test
if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))  # True
    print(s.containsDuplicate([1, 2, 3, 4]))  # False