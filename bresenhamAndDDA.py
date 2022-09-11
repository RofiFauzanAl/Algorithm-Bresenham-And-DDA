#Line_Bresenham
def lineBres(xa, ya, xb, yb):
    dx = abs(xa - xb)
    dy = abs(ya - yb)
    p = 2 * dy - dx
    twoDy = 2 * dy
    twoDyDx = 2 * (dy - dx)
    
    if xa > xb: 
        x = xb
        y = yb
        xEnd = xa
    else: 
        x = xa
        y = ya
        xEnd = xb
    
    print('(%d, %d)' % (x, y))
    
    while x < xEnd :
        x += 1
        if p < 0 :
            p += twoDy
        else : 
            y += 1
            p += twoDyDx
        print('(%d, %d)' % (x, y))

#Line_DDA
def lineDDA(xa, ya, xb, yb):
    dx = xb - xa
    dy = yb - ya
    x = xa
    y = ya
    
    if (abs(dx) > abs(dy)) :
        steps = abs(dx)
    else : 
        steps = abs(dy)
        
    xIncrement = dx/ float(steps)
    yIncrement = dy/ float(steps)
    
    
    for k in range(steps):
        x += xIncrement
        y += yIncrement
        print('(%d, %d)' % (x, y))

print('Line Bresenham')
lineBres(200,90,210,90)
print('Line DDA')
lineDDA(4,4,8,8)