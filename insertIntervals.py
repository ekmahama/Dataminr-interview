def insert(intervals, newInterval):
    """
    Given a set of non-overlapping intervals,
    insert a new interval into the intervals (merge if necessary).
    You may assume that the intervals were initially sorted according to their start times.
    """
    output = []
    intervals.append(newInterval)
    intervals = sorted(intervals, key=lambda x: x[0])

    for cur in intervals:
        if not output or output[-1][1] < cur[0]:
            output.append(cur)
        else:
            output[-1][1]=max(output[-1][1], cur[1])
    return output
