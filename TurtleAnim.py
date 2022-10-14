import turtle as t
import colorsys as c

t.tracer(20)
t.bgcolor('black')
t.setpos(0, -230)
r = 0
t.setup(800, 600)
t.width(20)
t.ht()

for i in range(2000):
    r += 0.01
    color = c.hsv_to_rgb(r, 1, 1)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(i, 120)
    t.circle(90, 90)
    t.circle(i, 120)
    t.end_fill()

t.done()