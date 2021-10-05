import math

prueba="0"
while prueba=="0":
    U=input("Introduzca el orden de su rotación:")
    U=(2*math.pi/int(U))/2
    for i in [1,2,3,4,6]:
        for j in [1,2,3,4,6]:
            V=(2*math.pi/i)/2
            W=(2*math.pi/j)/2
            c=(math.cos(W)+math.cos(U)*math.cos(V))/(math.sin(U)*math.sin(V))
            if abs(c)<=1:
                w=math.acos(c)
                print("Los ejes a", round(360*U/math.pi), "y", round(360*V/math.pi), "combinan para formar un eje de", round(360*W/math.pi), "grados, cruzandose a", 180*w/math.pi,"grados.")
                print("cos^2(w)=",c*c)
    prueba=input("Si desea finalizar el programa, introduzca 0. De lo contrario, introduzca cualquier otra cosa")
