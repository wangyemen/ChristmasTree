'''
相对于一版，二版有了颜色
那我们是否可以在细节一点呢？
答案是可以的！
'''

from turtle import *
import random
import time

n = 80.0
# 设置速度快
speed("fastest")
# 背景颜色 海贝壳色，偏粉色
screensize(bg='seashell')
left(90)
forward(3 * n)
color("orange", "yellow")
begin_fill()
left(126)

time.sleep(10)
for i in range(5):
    forward(n / 5)
    right(144)
    forward(n / 5)
    left(72)
end_fill()
right(126)
color("dark green")
backward(n * 4.8)

def tree(d, s):
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)

tree(15, n)
backward(n / 2)

for i in range(200):
    a = 200 - 400 * random.random()
    b = 10 - 20 * random.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()

    if random.randint(0, 1) == 0:
        color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)
time.sleep(3)