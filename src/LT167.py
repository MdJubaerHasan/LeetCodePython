def twoSum(numbers: list[int], target: int) -> list[int]:
    pointer_one = 0
    pointer_two = len(numbers)-1


    while pointer_two >= pointer_one:
        current_sum = numbers[pointer_one] + numbers[pointer_two]

        if current_sum > target:
            pointer_two -= 1
        elif current_sum < target:
            pointer_one += 1
        else:
            return [pointer_one+1, pointer_two+1]
    return []


print(twoSum([2,7,11,15], 9))