string1=input("Enter your string 1:")
string2=input("Enter your string 2:")
swap_str1=string1[0]+string2[1]+string1[2:]
swap_str2=string2[0]+string1[1]+string2[2:]
string3=swap_str1+" "+swap_str2
print(string3)
