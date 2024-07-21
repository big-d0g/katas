def add(nums: str, *args: str) -> int:
    if args:
        for a in args:
            nums = nums + "," + (str(a))

    if nums == "":
        return 0

    if not nums[-1].isnumeric():
        raise ValueError

    n_array = []

    for n in nums:
        if n.isnumeric():
            n_array.append(n)

    # re.split(r",|\n", nums)

    sum_of: int = 0

    for n in n_array:
        sum_of += int(n)

    return sum_of
