# Linear Search
def linear_search(array, value):
    idxs = []
    for idx in range(len(array)):
        if array[idx] == value:
            idxs.append(idx)
    return idxs


def main():
    lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]
    # Nearest Neighbor Interpolation
    for idx, value in enumerate(lst_data):
        if value == None:
            lst_data[idx] = lst_data[idx - 1]
    print(lst_data)


if __name__ == "__main__":
    main()
