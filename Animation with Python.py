import drawSvg as draw

# Draw a frame of the animation
def draw_frame(t):
    d = draw.Drawing(2, 5.00, origin=(-1,-1.05))
    d.setRenderSize(h=150)
    d.append(draw.Rectangle(-4, -4, 8, 10, fill='white'))
    d.append(draw.Rectangle(-1, -1.00, 8, 1.05, fill='brown'))
    t = (t + 1) % 2 - 1
    y = 4 - t**2 * 4
    d.append(draw.Circle(0, y, 1, fill='lime'))
    return d

with draw.animate_jupyter(draw_frame, delay=0.10) as anim:
# Or:
#with draw.animate_video('example6.gif', draw_frame, duration=0.05
#                       ) as anim:
    # Add each frame to the animation
    for i in range(40):
        anim.draw_frame(i/10)
    for i in range(40):
        anim.draw_frame(i/10)
    for i in range(40):
        anim.draw_frame(i/10)
