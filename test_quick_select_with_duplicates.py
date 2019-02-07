from quick_select_with_duplicates import QuickSelectWithDuplicates


def test_find_kth_largest_distinct():
    s = QuickSelectWithDuplicates()

    for nums in [None, []]:
        for k in range(5):
            assert s.find_kth_largest_distinct(nums, k) is None

    nums = [1]
    assert s.find_kth_largest_distinct(nums, 0) is None
    assert s.find_kth_largest_distinct(nums, 1) == 1
    assert s.find_kth_largest_distinct(nums, 2) is None

    nums = [3, 1, 2]
    assert s.find_kth_largest_distinct(nums, 0) is None
    assert s.find_kth_largest_distinct(nums, 1) == 3
    assert s.find_kth_largest_distinct(nums, 2) == 2
    assert s.find_kth_largest_distinct(nums, 3) == 1
    assert s.find_kth_largest_distinct(nums, 4) is None

    nums = [3, 2, 2, 5, 1, 1]
    assert s.find_kth_largest_distinct(nums, 0) is None
    assert s.find_kth_largest_distinct(nums, 1) == 5
    assert s.find_kth_largest_distinct(nums, 2) == 3
    assert s.find_kth_largest_distinct(nums, 3) == 2
    assert s.find_kth_largest_distinct(nums, 4) == 1
    assert s.find_kth_largest_distinct(nums, 5) is None

    nums = [4, 4, 3, 3, 3, 2, 2, 2, 5, 1, 1]
    assert s.find_kth_largest_distinct(nums, 0) is None
    assert s.find_kth_largest_distinct(nums, 1) == 5
    assert s.find_kth_largest_distinct(nums, 2) == 4
    assert s.find_kth_largest_distinct(nums, 3) == 3
    assert s.find_kth_largest_distinct(nums, 4) == 2
    assert s.find_kth_largest_distinct(nums, 5) == 1
    assert s.find_kth_largest_distinct(nums, 6) is None
