def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # Flatten recursively
        else:
            result.append(item)
    return result

# Example usage
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output = flatten(input_list)
print(output)  # Output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

def reverse_list(lst):
    reversed_lst = []
    for item in reversed(lst):  # Reverse the lst
        if isinstance(item, list):
            reversed_lst.append(reverse_list(item))  # Flatten recursively
        else:
            reversed_lst.append(item)
    return reversed_lst

# Example usage
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output = reverse_list(input_list)
print(output)  # Output: [[[7, 6, 5], [4, 3], [2, 1]]]