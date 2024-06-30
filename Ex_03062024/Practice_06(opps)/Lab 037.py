# Map
def double_me(num):
    return 2 * num

numbers = [1, 2, 3, 4,5, 6, 7, 8, 9, 10]
doubled = map(double_me, numbers)
print(list(doubled))