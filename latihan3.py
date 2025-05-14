"""
Remove duplicate
"""


class ListProcessor:
    def __init__(self, nums):
        self.nums = nums

    def remove_duplicates(self):
        seen = set()
        result = []
        for item in self.nums:
            if item not in seen:
                seen.add(item)
                result.append(item)
        self.nums = result


# Contoh penggunaan
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
processor = ListProcessor(nums)
processor.remove_duplicates()
print("nums tanpa duplikat:", processor.nums)
