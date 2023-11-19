def non_overlapping_intervals(intervals,N): 
    result = []
    

    intervals.sort(key = lambda x: x[0])
    for i in range(1,N): 

        prev = intervals[i -1][1]
        curr = intervals[i][0]


        if prev < curr: 
            result.append([prev, curr])


    for i in result:
        print(result)

arr = [ [ 1, 3 ], [ 2, 4 ],
        [ 3, 5 ], [ 7, 9 ] ]
    
N = len(arr)


non_overlapping_intervals(arr, N)