def sum_eo(n, t):
    nums = []
    for num in range(0,n):
        nums.append(num)
    print(nums)
    # if t == e, return sum all even natural numbers less than n
    if t == "e":
        print(nums[::2])
        print(sum(nums[::2]))
        return sum(nums[::2])
    if t == "o":
        print(nums[1::2])
        print(sum(nums[1::2]))
        return sum(nums[1::2])

# else if t == o, return sum of all odd natural number less than n

# else, return -1

sum_eo(13,"o")