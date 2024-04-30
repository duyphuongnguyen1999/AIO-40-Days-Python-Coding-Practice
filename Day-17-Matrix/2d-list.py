# Question 1
def main():
    lst_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    lst_sub_data = [[] for _ in range(len(lst_data))]
    for idx, item in enumerate(lst_data):
        lst_sub_data[idx].extend([lst_data[idx][0], lst_data[idx][2]])
    print(lst_sub_data)


if __name__ == "__main__":
    main()
