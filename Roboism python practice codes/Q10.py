x = int (input("Enter the value of x:"))
y = int (input ("Enter the value of y:"))
 
#using XOR 
x = x ^ y
y = x ^ y
x = x ^ y
 
print("New value of x is:", x)
print("New value of y is:", y)
