a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if b**2 - 4 * a * c > 0:
    x1 = ((-b + (b**2 - 4 * a * c > 0)**(1/2)) / (2 * a))
    x2 = ((-b - (b**2 - 4 * a * c > 0)**(1/2)) / (2 * a))
    print("Roots: " + str(x1), ', '+ str(x2))
elif b**2 - 4 * a * c == 0:
    x = -b / (2 * a)
    print("Roots: " + str(x))
else:
    print("No roots")