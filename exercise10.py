list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Filter odd numbers from list1 and even numbers from list2
odd_from_list1 = [number for number in list1 if number % 2 != 0]
even_from_list2 = [number for number in list2 if number % 2 == 0]

# Combine the filtered lists
result_list = odd_from_list1 + even_from_list2

# Print the result list
print("result list:", result_list)