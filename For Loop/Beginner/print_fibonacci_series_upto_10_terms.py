n = int(input("Enter Fibonacci Series Range: "))
a = 0
b = 1
print(a, end = " ")
print(b, end = " ")
for i in range(2,n):
    c = a + b
    print(c, end = " ")
    a = b
    b = c