def merge(intervals):
    """
    Given an array of intervals where intervals[i] = [starti, endi],
    merge all overlapping intervals, and return an array of the
    non-overlapping intervals that cover all the intervals in the input.
    """
    output = []
    intervals = sorted(intervals, key=lambda x: x[0])
    for cur in intervals:
        if not output:
            output.append(cur)
        elif output[-1][1] < cur[0]:
            output.append(cur)
        else:
            output[-1][1]=max(output[-1][1], cur[1])
    return output
