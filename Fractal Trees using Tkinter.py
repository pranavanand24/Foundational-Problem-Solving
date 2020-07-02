from turtle import * 
from random import *

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()

x = -200
turtles = [t1,t2,t3,t4,t5]
for t in turtles:
  t.speed(500)
  t.left(120)
  t.color('brown')
  t.pu()
  x += randint(100,160)
  t.goto(x, randint(-100,100))
  t.pd()


def branch(turt, branch_len):
  angle = randint(25,30)
  sf = uniform(0.6,0.8)
  size = int(branch_len /10)
  turt.pensize(size)
  if branch_len < 30:
    turt.color('green')
    turt.stamp()
    turt.color('brown')

  if branch_len > 10:
    turt.forward(branch_len)
    turt.left(angle)
    branch(turt, branch_len*sf)
    turt.right(angle*2)
    branch(turt, branch_len*sf)
    turt.left(angle)
    turt.backward(branch_len)

for t in turtles:
  branch(t,100)