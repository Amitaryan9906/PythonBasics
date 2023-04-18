# # i=2/0
# # print(i)
# try:
#     i = 2/0
# except ZeroDivisionError:
#     # print(i)
#     print("Error: Division by zero" )
#     a=10
#     b=6
#     print("Addition",a +b )
#     print("Subtraction", a - b)
#     print("Multiplication", a * b)
#     print("Division", a / b)
#
#     # print(type(a))
#     print(bool(a))
#     m="" #" R"
#     print(bool(m))
#     str="Aryan"
#     print(str[0])
#
#     print(str [::-1] == str) # Reverse and Checking palindrome
#
# # Multiple line String
# name="""Hi
# I
#
#
#
#
#
# Am
# Super
# Hero"""
#
# print("Supe" in name)
# print(len(name))
# print(name[4])
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.find('e'))
# print(name.count('m',2,11))
# print(name.isupper())
# print(name.islower())
# arr=name.split("Am")
# arr2=name.rsplit()
# print(arr)
# print(arr2)
#
# # Trimming
# s="    Hi   "
# print(s.strip())
# print(s.rstrip())
# print(s.lstrip())
#
# # Replaceing
# print(s.replace("i","j"))

# str=input("Enter a String")
#
# l=len(str)
# mid=l//2
#
# if l% 2==0:print(str[mid-1:mid+1])
# else:
#     print(str[mid])



s="Thiru vanantham puram"

print(s.upper())

count_v=s.count('v')
print(count_v)
rs=s [::-1]
print(rs)
ns=s.replace('i','j')
print(ns)
print(s[0:7]) # s[0:] is default value to print full string
print(s [::-1])
print(s.split()[-1])