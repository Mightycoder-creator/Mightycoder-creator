import turtle as t
import colorsys as cs
t.bgcolor("black")
n = 70
h = 0
for i in range(202020):
  t.pencolor(cs.hsv_to_rgbn(h, 0.8, 1)
             h+= 1/n
  t.circle(100)
  t.fd(1)
  t.rt(1)
