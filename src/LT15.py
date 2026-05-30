def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i, num in enumerate(nums):
        if i > 0:
            prev_num = nums[i - 1]
            if num == prev_num:
                continue
        num = num * (-1)
        ptr_one = i + 1
        ptr_two = len(nums) - 1

        while ptr_one < ptr_two:
            new_sum = nums[ptr_one] + nums[ptr_two]

            if new_sum > num:
                ptr_two = ptr_two - 1

            elif new_sum < num:
                ptr_one = ptr_one + 1
            else:
                result.append([nums[i], nums[ptr_one], nums[ptr_two]])
                while ptr_one < ptr_two and nums[ptr_one] == nums[ptr_one+1]:
                    ptr_one += 1
                while ptr_one < ptr_two and nums[ptr_two] == nums[ptr_two-1]:
                    ptr_two -= 1

                ptr_one += 1
                ptr_two -= 1
    return result

print(threeSum([1,2,0,1,0,0,0,0]))