# Question 2
import numbers


class MatrixManipulation:
    # Constructor
    def __init__(self, mat_a, mat_b):
        # Run validation to received arguments
        assert isinstance(
            mat_a, list
        ), f"mat_a must be a list, but received {type(mat_a)}"
        assert isinstance(
            mat_b, list
        ), f"mat_b must be a list, but received {type(mat_b)}"

        # Assign value for class attribute
        self.mat_a = mat_a
        self.mat_b = mat_b
        self.mat_a_shape = self._get_shape(self.mat_a)
        self.mat_b_shape = self._get_shape(self.mat_b)

    def _get_shape(self, matrix):
        nrows = len(matrix)
        ncols = len(matrix[0])
        shape = (nrows, ncols)
        return shape

    def matrix_addition(self):
        # Check if 2 matrixes in same shape
        assert (
            self.mat_a_shape == self.mat_b_shape
        ), "For addition operation, 2 matrixes must in same shape"
        # Matrix Addtition
        result = [
            [
                self.mat_a[row][col] + self.mat_b[row][col]
                for col in range(self.mat_a_shape[1])
            ]
            for row in range(self.mat_a_shape[0])
        ]
        return result

    def matrix_subtraction(self):
        # Check if 2 matrixes in same shape
        assert (
            self.mat_a_shape == self.mat_b_shape
        ), "For subtraction, 2 matrixes must in same shape"
        # Matrix Subtraction
        result = [
            [
                self.mat_a[row][col] - self.mat_b[row][col]
                for col in range(self.mat_a_shape[1])
            ]
            for row in range(self.mat_a_shape[0])
        ]
        return result

    def matrix_multiplication(self):
        assert (
            self.mat_a_shape[1] == self.mat_b_shape[0]
        ), "Number of columns in mat_a must equal to the number of rows in mat_b"

        result_nrows = self.mat_a_shape[0]
        result_ncols = self.mat_b_shape[1]
        result = [[0 for _ in range(result_ncols)] for _ in range(result_nrows)]

        for row in range(result_nrows):
            for col in range(result_ncols):
                for k in range(len(self.mat_a[0])):
                    result[row][col] += self.mat_a[row][k] * self.mat_b[k][col]
        return result

    def dot_product(self):
        # Run validation to received arguments
        assert isinstance(self.mat_a, list) and all(
            isinstance(x, numbers.Number) for x in self.mat_a
        ), "mat_a must be 1D-list (vector) with numeric elements for dot product"

        assert isinstance(self.mat_b, list) and all(
            isinstance(x, numbers.Number) for x in self.mat_b
        ), "mat_b must be 1D-list (vector) with numeric elements for dot product"

        assert len(self.mat_a) == len(
            self.mat_b
        ), "Vectors must have same length for dot product"

        # Dot Product
        result = 0
        for i in range(len(self.mat_a)):
            result += self.mat_a[i] + self.mat_b[i]
        return result


def main():
    mat_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat_b = [[2, 4, 6], [1, 3, 5], [1, 0, 1]]

    matrixes_obj = MatrixManipulation(mat_a, mat_b)

    print("Matrix Addition:\n", matrixes_obj.matrix_addition())
    print("Matrix Subtraction:\n", matrixes_obj.matrix_subtraction())
    print("Matrix Multiplication:\n", matrixes_obj.matrix_multiplication())
    # print("Matrix Dot Product:\n", matrixes_obj.dot_product())


if __name__ == "__main__":
    main()
