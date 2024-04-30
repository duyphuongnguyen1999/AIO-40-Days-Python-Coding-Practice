import os

# Create a list contains integer in range [1, 10]
lst_data = [x for x in range(1, 11)]

# Get current working file path
current_file_path = os.path.abspath(__file__)
# Get current directory
current_directory = os.path.dirname(current_file_path)
# Initialize data.txt file path
file_path = os.path.join(current_directory, "data.txt")
# Create a data to write to data.txt file
text = [str(x) for x in lst_data]  # Convert to str
text = "-".join(text)  # Join str

# Question 1: Write file
with open(file_path, "w") as file:
    file.write(text)

# Question 2: Read file
with open(file_path, "r") as file:
    data = file.read()
data = data.split("-")  # Split str
data = [int(x) for x in data]  # Convert to int
lst_filter = [x for x in data if x % 3 == 0]
print(lst_filter)
