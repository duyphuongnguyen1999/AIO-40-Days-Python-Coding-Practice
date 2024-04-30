class VectorManipulation:
    def __init__(self, vector_1, vector_2):
        # Assign values to class attributes
        self.vector_1 = vector_1
        self.vector_2 = vector_2

    def sum(self):
        assert len(self.vector_1) == len(
            self.vector_2
        ), "Vectors must be in same size for addition"
        result = (x + y for x, y in zip(self.vector_1, self.vector_2))
        return result

    def multiply(self):
        assert len(self.vector_1) == len(
            self.vector_2
        ), "Vectors must be in same size for addition"
        result = (x * y for x, y in zip(self.vector_1, self.vector_2))
        return result

    def distance(self):
        sum = 0
        for x, y in zip(self.vector_1, self.vector_2):
            sum += (x - y) ** 2
        result = sum**0.5
        return result


def main():
    print("Question 1:")
    my_tuple1 = (2, 3)
    my_tuple2 = (3, 6)
    print(f"{my_tuple1 = }")
    print(f"{my_tuple2 = }")

    vectors = VectorManipulation(my_tuple1, my_tuple2)

    print("Question 2:")
    print("Result_vector1 = ", vectors.sum())
    print("Result_vector2 = ", vectors.multiply())

    print("Question 3:")
    print("Distance: ", vectors.distance())

    print("my_tuple1 value=3 index: ", my_tuple1.index(3))
    print("my_tuple2 value=3 index: ", my_tuple2.index(3))


if __name__ == "__main__":
    main()
