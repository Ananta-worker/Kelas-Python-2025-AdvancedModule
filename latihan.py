"""
Remove all occurrences of val in nums in-place.
Shift the remaining elements to the front,
and fill the rest with 0 to maintain the length of nums.
Args:
    nums (list of int): input list
    val (int): value to remove

Returns:
    list: modified nums list
"""


class Solution(object):
    def remove_element(self, nums, val):

        k = 0
        for i in nums:      # untuk i dalam list nums, maka
            if i != val:    # jika i tdksama dengan val, maka
                nums[k] = i     # list nums di index ke k menjadi i
                k += 1      # k = +1

        for i in range(k, len(nums)):   # utk i dlm range(dari index k, sampai len:jumlah karakter list nums)
            nums[i] = 0                 # karakter dijadikan 0
        return nums                     # mengembalikan nilai nums


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 5, 4, 2]
    val = 2
    solution = Solution()
    result = solution.remove_element(nums, val)
    print(result)
