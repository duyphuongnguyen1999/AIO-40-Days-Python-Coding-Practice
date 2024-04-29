#  Question 1: Create a list range from 1-10
lst_data = [x for x in range(1, 11, 1)]
print(lst_data)

# Question 2: Extract first 5 elements of lst_data
print(lst_data[:5])

# Question 3: Print all odds in lst_data (using for loop)
odds = []
for ele in lst_data:
    if ele % 2 == 1:
        odds.append(ele)
print(odds)

# Question 4: Calculate sum of all elements in lst_data
sum = 0
for ele in lst_data:
    sum += ele
print(sum)
