"""
    Merge overlaping intervals
    example: merge([[1,3],[2,6],[8,10],[9,18]]))  # Output: [[1,6],[8,18]]

    assumptions:
     - there are not repeated intervals
     - intervals are always from low to high not for example [18 ,7] instead of [7, 18]
"""

def merge(intervals: list[list]) -> list[list]:
    # Order the intervals
    # Why using a tuple as the key istead of the list? is more efficiente because they are imutable and hashables
    # Like this it will sort lexicographically (1, 3) < (1, 5) or (a, b) < (a, c)
    intervals = sorted(intervals, key = lambda x: (x[0], x[1]))

    merged = []
    for interval in intervals:
        if not merged:
            merged.append(interval)
        else:
            last = len(merged)-1 
            if merged[last][1] > interval[0] and merged[last][1] < interval[1]:
                merged[last][1] = interval[1]
            elif merged[last][1] < interval[0]:
                merged.append(interval)
    return merged

if __name__ == '__main__':
    print(merge([[1,3],[2,6],[8,10],[15,18]]))

    # [1, 3], [2, 5], [2, 6], [7, 18], [8, 10]