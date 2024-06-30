number = [1,2,3,4,5,6,7,8,9,10]
def is_grater(num):
    return num > 5

grater_5 = filter(is_grater, number)
print(list(grater_5))

