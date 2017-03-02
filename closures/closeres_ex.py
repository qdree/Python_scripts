def sort_priority(values, group):
    found = [False]
    def helper(x):
        # nonlocal found
        if x in group:
            found[0] = True
            return (0,x)
        return (1,x)
    values.sort(key=helper)
    return found[0]


nums = [5,2,1,6,8,2,12,4,3,7]
group = {2,3,5,12}

sort_result = sort_priority(nums, group)
print nums, sort_result
