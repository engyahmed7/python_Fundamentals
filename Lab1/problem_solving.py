def diagonalDifference(arr):
    n = len(arr)
    first_sum = 0
    second_sum = 0
    for i in range(n):
        first_sum += arr[i][i];
        second_sum += arr[i][n - i - 1];
    return abs(first_sum - second_sum)
