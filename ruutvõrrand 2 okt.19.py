import math

a = int(input("enter the coefficients of a:"))
b = int(input("enter the coefficients of b:"))
c = int(input("enter the coefficients of c:"))

d = b**2-4*a*c # discriminant

if d < 0:
    print ("this equation has no real solution")
elif d== 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print("this equation has one solution"), x
else:
    x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    print("this equation has two solutions:", x1, "or", x2)
