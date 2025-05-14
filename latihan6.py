class MajorityElementFinder:
    def __init__(self, nums):
        self.nums = nums

    def find_majority_element(self):
        count = 0
        candidate = max(nums)

        count = sum(1 for num in self.nums if num == candidate)
        if count > len(self.nums) // 2:     # membagi jadi bil. bulat ke bawah
            return candidate
        else:
            return None


# Contoh penggunaan
nums = [1, 3, 3, 2, 3]
finder = MajorityElementFinder(nums)
majority_element = finder.find_majority_element()
if majority_element is not None:
    print(f"Elemen mayoritas adalah: {majority_element}")
else:
    print("Tidak ada elemen mayoritas.")