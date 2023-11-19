def insert_interval(intervals, new_interval): 

    intervals = sorted(intervals + [new_interval])
    # [intervals + new interval].sorted(key = lambda x: x[0])

    result = [intervals[0]]

    for i in range(len(intervals)): 
        if result[-1][-1] >= intervals[i][0]:
            result[-1] = [min(result[-1][0], intervals[i][0]), max(result[-1][1], intervals[i][1])]

        else: 
            result.append(intervals[i])

    return result 


intervals = [[1,3],[6,9]] 
new_interval = [2,5]


print(insert_interval(intervals, new_interval))