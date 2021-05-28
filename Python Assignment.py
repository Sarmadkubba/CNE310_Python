def lone_sum(a, b, c):
<<<<<<< HEAD
    if a == b and b == c:
        return 0
=======
    if a >= b:
        return c
>>>>>>> 14a1a2749ffaf07602916731647a940593394fda
    elif a == c:
        return b
    elif b == c:
        return a
<<<<<<< HEAD
    elif a == b:
        return c
    else:
        return a + b + c
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    result = lone_sum(x, y, z)
    print("Input: " + str(x) + ", " + str(y) + ", " + str(z))
    print("Result: " + str(result))
=======
    elif a == b and a == c and b == c:
        return 0
    else:
        return a+b+c
>>>>>>> 14a1a2749ffaf07602916731647a940593394fda
