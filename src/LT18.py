class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        size = len(nums)
        # We use 2 nested loops
        for i in range(size-3):

            # we check if we can even form the target :

            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break

            # We also check if this i is a valid candidate:

            if nums[i] + nums[size-1] + nums[size-2] + nums[size-3] < target:
                continue

            # Duplicate avoided
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, size-2):

                # Matching i while avoiding duplicates
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left_ptr = j+1
                right_ptr = size-1


                current_sum = target - (nums[i] + nums[j])

                while left_ptr < right_ptr:
                    new_sum = nums[left_ptr] + nums[right_ptr]

                    if new_sum < current_sum:
                       left_ptr += 1
                    elif new_sum > current_sum:
                        right_ptr -= 1
                    else:
                        res.append([nums[i], nums[j],nums[left_ptr], nums[right_ptr]])
                        while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr+1]:
                            left_ptr += 1
                        while left_ptr < right_ptr and nums[right_ptr] == nums[right_ptr-1]:
                            right_ptr -= 1

                        left_ptr += 1
                        right_ptr -= 1
        return res




