# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if len(numbers) == 0:
        return (None, None)
    
    if len(numbers) == 1:
        return(numbers[0], None)
    
    max_value = max(numbers)

    lower_values = [x for x in numbers if x < max_value]

    second_max = max(lower_values)

    return(max_value, second_max)
print(max_two_in_list([1, 3, 2, 5, 4]))

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    unique_list = list(set(numbers))
    
    sorted_list = sorted(unique_list)
    
    return sorted_list

print(remove_duplicates_and_sort([3, 1, 2, 3, 1]))
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    current_sum = 0

    for num in arr:
        current_sum += num
        result.append(current_sum)
    return result
print(cumulative_sum([1, 2, 3, 4]))



# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    result = []
    rows = len(matrix)
    column = len(matrix[0])

    for num in range(column):
        new_row = []

        for r in range(rows):
            new_row.append(matrix[r][num])
        result.append(new_row)
    return result
print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return lst[::step]
print(slice_every_nth([1, 2, 3, 4, 5, 6], 2))

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
   return sum(a * b for a, b in zip(list1, list2))

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    rows_1 = len(matrix1)
    column_1 = len(matrix1[0])
    column_2 = len(matrix2[0])

    result = []

    for i in range(rows_1):
        new_row = []
        for j in range(column_2):
            current_sum = 0
            for k in range(column_1):
                current_sum += matrix1[i][k] * matrix2[k][j]
            new_row.append(current_sum)
        result.append(new_row)
    return result
print(matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]))