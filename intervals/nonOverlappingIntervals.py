def soln(intervals):
    intervals.sort()
    
    current_end = intervals[0][1]

    number_of_intervals_removed = 0

    for interval in intervals[1:]:
        start = interval[0]
        end = interval[1]

        if current_end <= start:
            current_end = end
        else:
            # remove interval that has the longer end 
            current_end = min(end, current_end)
            number_of_intervals_removed += 1

    return number_of_intervals_removed


intervals = [[1,2],[2,3],[3,4],[1,3]]
print(soln(intervals))