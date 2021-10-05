import math


U=(2*math.pi/3)/2
for i in [1,2,4,6]:
    for j in [1,2,4,6]:
        V=(2*math.pi/i)/2
        W=(2*math.pi/j)/2
        c=(math.cos(W)+math.cos(U)*math.cos(V))/(math.sin(U)*math.sin(V))
        if abs(c)<=1:
            w=math.acos(c)
            print("Los ejes a", round(360*U/math.pi), "y", round(360*V/math.pi), "combinan para formar un eje de", round(360*W/math.pi), "grados, cruzandose a", 180*w/math.pi,"grados")
            print(c*c)
