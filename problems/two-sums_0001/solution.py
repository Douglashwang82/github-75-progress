def two_sum_hash_map_solution(nums, target):
    """
    Hash map approach
    Time: O(n), where n is the length of nums. Each lookup and insertion in the hash map is O(1).
    Space: O(n), for storing up to n elements in the hash map.
    """
    num_to_index = {}
    for index, num in enumerate(nums):
        completment = target - num
        if completment in num_to_index:
            return [num_to_index[completment], index]
        num_to_index[num] = index   
    return []

def two_sum_brute_force_solution(nums, target):
    """
    Brute force approach
    Time: O(n^2), where n is the length of nums. Each pair is checked.
    Space: O(1), no extra space is used except for the output list.
    """
    for index_x in range(len(nums)):
        for index_y in range(index_x + 1, len(nums)):
            if nums[index_x] + nums[index_y] == target:
                return [index_x, index_y]
    return []

def two_sum_linear_search_solution(nums, target):
    """
    Linear search approach
    Time: O(n^2), where n is the length of nums. Each pair is checked.
    Space: O(1), no extra space is used except for the output list."""
    for index_x in range(len(nums)):
        complement = target - nums[index_x]
        for index_y in range(index_x + 1, len(nums)):
            if nums[index_y] == complement:
                return [index_x, index_y]
    return []

def two_sum_binary_search_solution(nums, target):
    """
    Binary search approach
    Time: O(n log n), where n is the length of nums.
    Space: O(n), for storing the sorted list of tuples (num, index).
    """
    nums_with_indices = sorted((num, idx) for idx, num in enumerate(nums))
    for i, (num, idx1) in enumerate(nums_with_indices):
        complement = target - num
        left, right = i + 1, len(nums_with_indices) - 1
        while left <= right:
            mid = (left + right) // 2
            num_mid, idx2 = nums_with_indices[mid]
            if num_mid == complement:
                return [idx1, idx2]
            elif num_mid < complement:
                left = mid + 1
            else:
                right = mid - 1
    return []
                
def two_sum_two_pointers_solution(nums, target):
    """
    Two pointers approach
    Time: O(n log n), where n is the length of nums due to sorting.
    Space: O(1), no extra space is used except for the output list.
    """
    nums_with_indices = sorted((num, idx) for idx, num in enumerate(nums))
    left, right = 0, len(nums_with_indices) - 1
    while left < right:
        current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
        if current_sum == target:
            return [nums_with_indices[left][1], nums_with_indices[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []    

if __name__ == "__main__":
    nums = [3, 3, 3, 3, 3, 3, 3, 3, 4]
    target = 6

    print("Using hash map solution")
    print(two_sum_hash_map_solution(nums, target))  

    print("Using brute force solution")
    print(two_sum_brute_force_solution(nums, target))

    print("Using linear search solution")
    print(two_sum_linear_search_solution(nums, target))

    print("Using binary search solution will not return the first pair if there are duplicates") 
    print(two_sum_binary_search_solution(nums, target))

    print("Using two pointers solution will not return the first pair if there are duplicates")
    print(two_sum_two_pointers_solution(nums, target))