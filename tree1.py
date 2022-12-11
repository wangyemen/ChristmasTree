'''
绘制一颗圣诞树
'''
# 设置圣诞树的基本结构
height = 5
stars = 1

for i in range(height):
    print((" " * (height - i) + ("*" * stars)))
    stars += 2

print((" " * height) + "|")