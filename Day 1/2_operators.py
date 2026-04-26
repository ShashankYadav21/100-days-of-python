# Arithmetic operators
a = 6
b = 2
c = a+b
print(c)
c = a-b
print(c)
c = a/b
print(c)
c = a*b
print(c)
c = a%b #Modulus
print(c)
c = a**b #Power
print(c)
c = a//b #Floor Division
print(c)

# Assignment Operators

d = 10-6 # Assign 10-6 to d

d += 3 # Increment the value of d by 3 and then assign the new value to d
d -= 3 # Decrement the value of d by 3 and then assign the new value to d
d /= 3 # Divide the value of d by 3 and then assign the new value to d
d //= 3 # Floor Division of d by 3 and then assign the new value to d
d *= 3 # Multiply the value of d by 3 and then assign the new value to d
d **= 3 # d raise to the power 3 and then assign the new value to d
d %= 3 # remainder and then assign the new value to d

# Comparison Operators

5 == 5   # True (Equal to)
5 == 3   # False

5 != 3 #(not Equal to) True
5 != 5 #(not Equal to) False

# Greater than and Less than

7>5 # True
7>=5 # True
7<5 # False
7<=5 # False

#Note  - Floating point number is invalid in comparison operators due to precision issues

# Logical Operators : or & and

e = True or False

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and' 
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

