# Create an empty list called my_list
my_list = []
print(f"Initial empty list: {my_list}") #Output the initial empty list

# Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"List after appending: {my_list}") #Output the list after appending elements

# Insert the value 15 at the second position in the list (index 1)
my_list.insert(1, 15) #insert(index, element)
print(f"List after inserting 15: {my_list}") #Output the list after inserting

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print(f"List after extending: {my_list}") #Output the list after extending

# Remove the last element from my_list
my_list.pop() #Removes the last element by default.
print(f"List after removing last element: {my_list}") #Output the list after pop

# Sort my_list in ascending order
my_list.sort()
print(f"List after sorting: {my_list}") #Output the sorted list

# Find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print(f"Index of 30: {index_30}") #Output the index of 30
