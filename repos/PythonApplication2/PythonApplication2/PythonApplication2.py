import turtle
def bresenham_line(x1, y1, x2, y2)
dx = abs(x2 - x1)
dy = abs(y2 - y1)
x_step = 1 If x1<x2 Else -1
y_step = 1 If y1<y2 Else -1
Error= 2 * dy_dx
Line_points =[]
x,y= x1.y1
for_inrange(dx + 1)
line_points.append((x, y))
If error>0;
    y += y_step
Error-=2*dx
    Error+=2*dy
    x += x_step
Return line_points
turtle.setup(500, 500)
turtle.speed(0)
x1.y1 = 100,100
    x2, y2 = 400, 300
    line_points = bresenham_line(x1, y1, x2, y2)
turtle.peneep()
turtle.goto(x1, y1)
turtle.pendown()
For x,y in line_points;
    turtle.goto(x, y)
turtle.exitonclick()
