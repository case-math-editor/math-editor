def is_present_in_matrix(matrix: list[list[int]], target: int) -> bool:
    """Check if elements present in sorted matrix in log(n) time"""

    left = 0
    right = len(matrix) * len(matrix[0]) - 1

    while True:
        middle = (left + right) // 2

        row = middle // len(matrix[0])
        column = middle % len(matrix[0])

        if left > right:
            return False
        elif left == right:
            return matrix[row][column] == target

        if matrix[row][column] == target:
            return True
        elif matrix[row][column] < target:
            left = middle + 1
        else:
            right = middle - 1
