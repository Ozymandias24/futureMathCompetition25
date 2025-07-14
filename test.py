import cmath
import turtle as t
import matplotlib as plt

def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def isFprime(p):
    if p < 3: return False
    m = 0
    while True:
        fermat = 2 ** (2 ** m) + 1
        if fermat == p:
            return is_prime(p)
        if fermat > p:
            return False
        m += 1


def get_CircleUnit(n):
    return [cmath.exp(2j * cmath.pi * k / n) for k in range(n)]


n = int(input("Enter the number of angles: "))
print(isFprime(n))

tmp = get_CircleUnit(n)
print(tmp)

points = []
obj = t.Turtle()

obj.hideturtle()
obj.speed(0)
obj.pensize(2)

# x축
obj.penup()
obj.goto(-300, 0)
obj.pendown()
obj.goto(300, 0)

# y축
obj.penup()
obj.goto(0, -300)
obj.pendown()
obj.goto(0, 300)

# 축 레이블 추가
obj.penup()
obj.goto(310, -10)
obj.write("Re", font=("Arial", 12, "bold"))
obj.goto(10, 310)
obj.write("Im", font=("Arial", 12, "bold"))
obj.speed(1)

obj.pensize(1)

obj.penup()
obj.goto(100, 0)

obj.pendown()
for i in tmp[1:]:
    points.append((i.real*100, i.imag*100))
    obj.goto(i.real*100, i.imag*100)
    
    
    
obj.goto(100, 0)
obj.penup()

for i in tmp:
    x = i.real*100
    y = i.imag*100
    obj.goto(x, y)
    obj.dot(5, "red")
    obj.goto(x+10, y+10)
    x /= 100
    y /= 100

    obj.write(f"{x:.2f}, {y:.2f}i", font=("Arial", 10, "normal"))

obj.write(f"")


t.done()
input("Press Enter to Exit...")





# def factorize(n):
#     k = 0
#     while n % 2 == 0:
#         n //= 2
#         k += 1
#     ps = []
#     i = 3
#     while i * i <= n:
#         if n % i == 0:
#             if is_prime(i): ps.append(i)
#             while n % i == 0: n //= i
#         i += 2
#     if n > 1:
#         if is_prime(n): ps.append(n)
#     return k, ps