def main():
    # Question 1: Create a list named lst_data contains integers from 1 to 10
    lst_data = [num for num in range(1, 11, 1)]
    print(lst_data)

    # Question 2: Calculate Median of the list
    def calculate_median(lst_data):
        if len(lst_data) % 2 == 0:  # If num of elements in lst_data is even
            index = int(len(lst_data) / 2)
            median = (lst_data[index] + lst_data[index + 1]) / 2
        else:  # If num of elements in lst_data is odd
            index = (len(lst_data) + 1) / 2
            median = lst_data[index]
        return median

    print(f"Median: {calculate_median(lst_data)}")

    # Question 3: Filter all odd in lst_data as lst_odd_filter, sort descending
    lst_data_filter = [odd for odd in lst_data if odd % 2 == 1]
    lst_data_filter.sort(reverse=True)
    print(lst_data_filter)


if __name__ == "__main__":
    main()
