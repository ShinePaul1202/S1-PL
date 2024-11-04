lst1=input("Enter list1 elements by space seperated :").split()
lst2=input("Enter list2 elements by space seperated :").split()
print("output list :")
print(list(set(lst1)-set(lst2)))
