# Question 2
def matrix_manipulation(mat_a, mat_b, cal_type="add"):
    cols = len(mat_a[0])
    rows = len(mat_a)
    result = [[None for _ in range(cols)] for _ in range(rows)]
    match cal_type:
        case "add":
            for row_idx in range(rows):
                for col_idx in range(cols):
                    result[row_idx][col_idx] = (
                        mat_a[row_idx][col_idx] + mat_b[row_idx][col_idx]
                    )
        case "subtract":
            for row_idx in range(rows):
                for col_idx in range(cols):
                    result[row_idx][col_idx] = (
                        mat_a[row_idx][col_idx] - mat_b[row_idx][col_idx]
                    )
        case "dot":
            result = 0
            for row_idx in range(rows):
                for col_idx in range(cols):
                    multiply = mat_a[row_idx][col_idx] * mat_b[row_idx][col_idx]
                    result += multiply
    return result


def main():
    mat_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat_b = [[2, 4, 6], [1, 3, 5], [1, 0, 1]]
    add_result = matrix_manipulation(mat_a, mat_b, "add")
    subtract_result = matrix_manipulation(mat_a, mat_b, "subtract")
    dot_product = matrix_manipulation(mat_a, mat_b, "dot")
    print(f"Add: {add_result}")
    print(f"Subtract: {subtract_result}")
    print(f"Dot: {dot_product}")


if __name__ == "__main__":
    main()
