"""
Assume the input array contains duplicates. The instinct is to de-duplicate first then apply quick-select. The
following avoid the deduplicate approach and performs quick-select directly.
"""


class QuickSelectWithDuplicates:
    def find_kth_largest_distinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or k <= 0:
            return
        elif self._find_n_uniques(nums, 0, len(nums) - 1) < k:
            return

        return self._quick_select(nums, 0, len(nums) - 1, k)

    def _quick_select(self, nums, start, end, k):
        # piv_idx_s, piv_idx_e: the correct indices range of nums[start] if sorted
        # Need the indices range in case the pivot number has duplicates
        piv_idx_s, piv_idx_e = self._partition(nums, start, end)
        n_uniques = self._find_n_uniques(nums, start, piv_idx_s - 1)
        if n_uniques == k - 1:
            return nums[piv_idx_s]
        elif n_uniques < k - 1:
            return self._quick_select(nums, piv_idx_e + 1, end, k - n_uniques - 1)
        else:
            return self._quick_select(nums, start, piv_idx_s - 1, k)

    def _partition(self, nums, start, end):
        piv = nums[start]
        gt = i = start
        lt = end
        while i <= lt:
            if nums[i] == piv:
                i += 1
            elif nums[i] > piv:
                nums[i], nums[gt] = nums[gt], nums[i]
                i += 1
                gt += 1
            else:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt -= 1
        return gt, lt

    def _find_n_uniques(self, nums, start, end):
        num_set = set()
        for i in range(start, end + 1):
            num_set.add(nums[i])
        return len(num_set)
