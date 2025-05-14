"""
Menghapus nilai tertentu dalam list
"""
class ListProcessor:
    def __init__(self, nums, nums2, val):
        self.nums = nums
        self.nums2 = nums2
        self.val = val

    def remove_val(self):
        self.nums = [x for x in self.nums if x != self.val]
        self.nums2 = [x for x in self.nums2 if x != self.val]

    def combine(self):
        return self.nums + self.nums2


# Example usage
nums = [2, 3, 3, 4, 7, 8]
nums2 = [2, 4, 5, 1, 3, 2]
val = 3
processor = ListProcessor(nums, nums2, val)
processor.remove_val()
nums3 = processor.combine()
print("nums3:", nums3)

# slicing
# Daftar awal
nums = [2, 3, 3, 4, 7, 8]
# Menghapus 2 angka di depan dan 1 angka di belakang
nums = nums[2:-1]
# Menampilkan hasil
print("nums:", nums)


# menggunakan metode class
class ListProcessor:
    def __init__(self, nums):
        self.nums = nums

    def remove_val(self):
        self.nums = nums[2: -1]
        return self.nums

    def menampilkan(self):
        return self.nums


# Example usage
nums = [2, 3, 3, 4, 7, 8, 9]
processor = ListProcessor(nums)
processor.remove_val()
nums = processor.menampilkan()
print("menggunakan fungsi class")
print("nums: ", nums)
