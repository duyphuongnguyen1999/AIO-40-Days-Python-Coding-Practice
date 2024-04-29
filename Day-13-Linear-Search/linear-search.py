# Linear Search
def linear_search(array, value):
    idxs=[]
    for idx in range(len(array)):
        if array[idx]==value:
            idxs.append(idx)
    return idxs

def main():
    lst_data=[1, 1.1, None, 1.4,
              None, 1.5, None, 2.0]
    none_idxs=linear_search(lst_data,
    	                      None)
    print(
    	f"Vị trí None đầu tiên: {none_idxs[0]}")
    print(
    	f"Danh sách các vị trí có giá trị None: {none_idxs}")

if __name__=="__main__":
    main()
    
    