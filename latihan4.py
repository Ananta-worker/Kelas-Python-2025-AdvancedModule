"""
Number limiter
"""

class NumberLimiter:
    def __init__(self, nums):
        self.nums = nums

    def limit_numbers(self):
        # Menghitung frekuensi setiap angka
        frequency = {}
        result = []
        for num in self.nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

            # Tambahkan ke hasil jika frekuensi kurang dari atau sama dengan 2
            if frequency[num] <= 2:
                result.append(num)
        return result


# Contoh penggunaan
nums = [0, 0, 2, 2, 2, 2, 3, 5, 7, 7, 7]
limiter = NumberLimiter(nums)
limited_nums = limiter.limit_numbers()
print(limited_nums)