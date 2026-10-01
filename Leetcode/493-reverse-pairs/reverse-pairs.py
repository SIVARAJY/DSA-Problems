class Solution:
    def merge(self, nums, low, mid, high):
        count = 0
        res = []

        j = mid + 1

        for i in range(low, mid + 1):
            while j <= high and nums[i] > 2 * nums[j]:
                j += 1

            count += j - (mid + 1)

        i = low
        j = mid + 1

        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j += 1

        while i <= mid:
            res.append(nums[i])
            i += 1

        while j <= high:
            res.append(nums[j])
            j += 1

        for i in range(low, high + 1):
            nums[i] = res[i - low]

        return count

    def mergecount(self, nums, low, high):
        if low >= high:
            return 0

        mid = (low + high) // 2

        count = self.mergecount(nums, low, mid)
        count += self.mergecount(nums, mid + 1, high)

        count += self.merge(nums, low, mid, high)

        return count

    def reversePairs(self, nums: list[int]) -> int:
        return self.mergecount(nums, 0, len(nums) - 1)