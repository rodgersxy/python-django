# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).
# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

def sum_array(arr):

    if arr is None or len(arr) <= 1:
        return 0
    
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)

    # Sum all elements and subtract the minimum and maximum values
    return sum(arr) - min_val - max_val         