#string in python are immutable

name1 = "Saurabh"
name2 = 'Singh'
print(name1)
print(name2)

#slice method

print(name1[0:3]) # start from 0  and go till 3-1
#print(name[a:b]) => start from a and go till b-1
print(name1[1:6])

print(name1.upper()) # make uppercase name1
print(name1.capitalize()) # capitalize first letter of name1
print(name1.count('a')) #count a in name1

number = "7"
print(number.isnumeric()) #check that it is number or not
print(name2.isnumeric())

harry = 3
Harry = 7

a1 = "harry"
a2 = 'harry'
a3 = '''harry
is a good boy ''' #this is used to write multi line comments
print(a1, a2, a3)