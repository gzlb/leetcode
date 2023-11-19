def merge_intervals(intervals): 

    intervals.sort(key = lambda x: x[0])
    result = [intervals[0]]
    

    for i in intervals: 
        if result[-1][-1] < i[0]: 
            result.append(i)

        else: 
            result[-1][-1] = max(result[-1][-1], i[-1])

    
    return result