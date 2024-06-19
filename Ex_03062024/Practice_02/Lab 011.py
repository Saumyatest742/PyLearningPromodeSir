#None data type
val=None
print(val)

# List - List of items
shopping_list=["milk","eggs","bread"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[-1])
print(type(shopping_list))

shopping_list .append("butter") #Add item in the end
print(shopping_list)
shopping_list.insert(1,"Lassi")
print(shopping_list)
shopping_list.extend(["Mayo", "Curd"]) # Adding another list in the end
print(shopping_list)
shopping_list.remove("Mayo") # Remove item
print(shopping_list)
shopping_list.reverse()
print(shopping_list)
shopping_list.sort()
print(shopping_list)


