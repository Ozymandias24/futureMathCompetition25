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

roots = get_CircleUnit(n)


points = []
obj = t.Turtle()
screen = t.Screen()

obj.hideturtle()
obj.speed(0.1)
obj.pensize(2)

# 축 레이블 추가
def draw_axes():
    obj.penup()
    obj.goto(-300, 0)
    obj.pendown()
    obj.goto(300, 0)
    obj.penup()
    obj.goto(0, -300)
    obj.pendown()
    obj.goto(0, 300)
    obj.penup()
    obj.goto(310, -10)
    obj.write("Re", font=("Arial", 12, "bold"))
    obj.goto(10, 310)
    obj.write("Im", font=("Arial", 12, "bold"))
    obj.penup()

obj.pensize(1)

def draw_polygon():
    obj.penup()
    start = roots[0]
    obj.goto(start.real * 100, start.imag * 100)
    obj.pendown()
    for z in roots[1:] + [start]:
        obj.goto(z.real * 100, z.imag * 100)
    obj.penup()
    

mode = 0

def draw_labels():
    obj.clear()
    draw_axes()
    draw_polygon()
    for k, z in enumerate(roots):
        x = z.real * 100
        y = z.imag * 100
        obj.goto(x, y)
        obj.dot(5, "red")
        obj.goto(x + 10, y + 10)
        if mode == 0:
            label = f"({z.real:.2f}, {z.imag:.2f}i)"
        elif mode == 1:
            r = abs(z)
            theta = cmath.phase(z)
            label = f"{r:.2f}(cos({theta:.2f}) + i·sin({theta:.2f}))"
        elif mode == 2:
            label = f"e^({2*k}πi/{n})"
        obj.write(label, font=("Arial", 10))


def switch_mode():
    global mode
    mode = (mode + 1) % 3
    draw_labels()

draw_axes()
draw_polygon()
draw_labels()
screen.listen()
screen.onkey(switch_mode, "space")

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