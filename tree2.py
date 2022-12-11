'''
感觉上一个太简单了
没关系我们还有二版的！
单词拓展：
circle 圆
square 正方形
导入的库有turtle
'''
import time
import turtle

# 先创建一个窗口
screen = turtle.Screen()
screen.setup(800, 600)

time.sleep(5)
# 绘制圣诞树的基本结构
circle = turtle.Turtle()
# 绘制圆形的速度、颜色、形状
circle.speed('fastest')
circle.color('red')
circle.shape('circle')
# 落笔
circle.up()

# 绘制正方形
square = turtle.Turtle()
square.speed('fastest')
square.shape('square')
square.color('green')
# 落笔
square.up()

#跳到指定坐标位置
circle.goto(0,280)
#复制当前图形
circle.stamp()
k = 0
for i in range(1, 17):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()
    if i % 4 == 0:
        x = 30*(j+1)
        circle.color('red')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()
        k += 2
    if i % 4 == 3:
        x = 30*(j+1)
        circle.color('yellow')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()
square.color('brown')

for i in range(17,20):
    y = 30*i
    for j in range(3):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()
turtle.exitonclick()