# Question 1: Create a list contains even number range from 1-12
lst_data = [even for even in range(1, 13, 1) if even % 2 == 0]
print(lst_data)

# Question 2: Remove all number which is divicible by 3
lst_data = [ele for ele in lst_data if ele % 3 != 0]
print(lst_data)

# Question 3:
# Add 1, 2, 3 to the end of lst data
for num in range(1, 4):
    lst_data.append(num)
# Other solution
# lst_data.extend(range(1, 4))

# Add 6, 7, 8 to position index = 3 of lst_data
index = 3
for num in range(6, 9, 1):
    lst_data.insert(index, num)
    index += 1
print(lst_data)

# Question 4: Update value of element which is divicible by 2 or 5 to 0
for idx in range(len(lst_data)):
    if (lst_data[idx] % 2 == 0) or (lst_data[idx] % 5 == 0):
        lst_data[idx] = 0
print(lst_data)
