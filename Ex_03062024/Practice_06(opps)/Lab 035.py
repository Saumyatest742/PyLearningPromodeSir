# Filter in python
# Aloow you to fliter the element in list, Tuple and set

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#filter on above list --> Even numbers
def even(num):
    return num % 2 == 0
even_number = filter(even, number)
print(list(even_number))