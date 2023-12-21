# list
# Creating a list
my_list = [1, 2, 3, "apple", "banana"]

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: "banana"

# Modifying elements
my_list[2] = 4
print(my_list)  # Output: [1, 2, 4, "apple", "banana"]

# Adding elements
my_list.append("orange")
print(my_list)  # Output: [1, 2, 4, "apple", "banana", "orange"]

# Removing elements
my_list.remove("apple")
print(my_list)  # Output: [1, 2, 4, "banana", "orange"]
