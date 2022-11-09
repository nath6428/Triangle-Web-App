
from sympy import *

def Calc(valList):
    
    global a,b,c,A,B,C, equations, values,emptyVals
    
    a = Symbol('a', positive = True, real = True, nonzero = True)
    b = Symbol('b', positive = True, real = True, nonzero = True)
    c = Symbol('c', positive = True, real = True, nonzero = True)

    A = Symbol('A', positive = True, real = True, nonzero = True)
    B = Symbol('B', positive = True, real = True, nonzero = True)
    C = Symbol('C', positive = True, real = True, nonzero = True)
        
    
    
    values = {
        
        0:a,
        1:b,
        2:c,
        3:A,
        4:B,
        5:C
        
    }
    
    emptyVals = {
        
        a:0,
        b:1,
        c:2,
        A:3,
        B:4,
        C:5     
                
    }


    
    
    for i in range(6):
        if valList[i] != '':
            values[i] = (int(valList[i]))

    a, b, c = values[0], values[1], values[2]
    A, B, C = values[3], values[4], values[5]
        
    conditions =[
        
        #SSS
        all(isinstance(i,int) for i in (a,b,c)),
        #SAS
        all(isinstance(i,int) for i in (A,b,c)),
        all(isinstance(i,int) for i in (A,a,b)),
        all(isinstance(i,int) for i in (A,a,c)),
        all(isinstance(i,int) for i in (B,b,c)),
        all(isinstance(i,int) for i in (B,b,a)),
        all(isinstance(i,int) for i in (B,b,c)),
        all(isinstance(i,int) for i in (C,a,b)),
        all(isinstance(i,int) for i in (C,c,a)),
        all(isinstance(i,int) for i in (C,c,b)),
        #SAA
        all(isinstance(i,int) for i in (A,b,C)),
        all(isinstance(i,int) for i in (A,a,B)),
        all(isinstance(i,int) for i in (A,a,C)),
        all(isinstance(i,int) for i in (B,b,A)),
        all(isinstance(i,int) for i in (B,b,C)),
        all(isinstance(i,int) for i in (C,c,A)),
        all(isinstance(i,int) for i in (C,c,B)),
        all(isinstance(i,int) for i in (B,a,C)),
        all(isinstance(i,int) for i in (A,c,B))
    ]

    if conditions[0]:
        print("1")
        equations = [
            Eq(((b**2 + c**2 - a**2)/(2*b*c)),cos(rad(A))),
            Eq(b*sin(rad(A))/a, sin(rad(B))),
            Eq(A+B+C, 180),
        ]
        return solver(equations)

    if conditions[1] or conditions[2] or conditions[3]:
        print("2")
        equations = [
            Eq((b**2 + c**2 - 2*b*c*cos(rad(A))), a**2),
            Eq(a*sin(rad(B))/b, sin(rad(A))),
            Eq(A+B+C, 180)
        ]
        return solver(equations)
    
    if conditions[4] or conditions[5] or conditions[6]:
        print("3")
        equations = [
            Eq((a**2 + c**2 - 2*a*c*cos(rad(B))), b**2),
            Eq(c*sin(rad(B))/b, sin(rad(C))),
            Eq(A+B+C, 180)
        ]
        return solver(equations)
    
    if conditions[7] or conditions[8] or conditions[9]:
        print("4")
        equations = [
            Eq((b**2 + c**2 - 2*b*c*cos(rad(A))), a**2),
            Eq((a**2 + c**2 - 2*a*c*cos(rad(B))), b**2),
            Eq((a**2 + b**2 - 2*a*b*cos(rad(C))), c**2),
            Eq(b*sin(rad(C))/c, sin(rad(B))),
            Eq(A+B+C, 180)
        ]
        return solver(equations)    
        
    if conditions[10:18]:
        print("5")
        equations = [
            Eq(A+B+C, 180)
        ]
        
        if isinstance(a, int):
            equations.append(Eq(b, a*sin(rad(B)/sin(rad(A)))))
            equations.append(Eq(c, a*sin(rad(C)/sin(rad(A)))))
            
        if isinstance(b, int):
            equations.append(Eq(a, b*sin(rad(A)/sin(rad(B)))))
            equations.append(Eq(c, b*sin(rad(C)/sin(rad(B)))))
            
        if isinstance(c, int):
            equations.append(Eq(b, c*sin(rad(B)/sin(rad(C)))))
            equations.append(Eq(a, c*sin(rad(A)/sin(rad(C)))))
            
            
        return solver(equations)
    
   
   
def test(value):
    global emptyVals    
    for i,j in list(emptyVals.items()):
        emptyVals[i] = list(value.values())[j]
    return emptyVals
   
def solver(equations):     
    
    global a,b,c,A,B,C, values
    x = solve(equations)
    values = test(values)
    if isinstance(x, list):
        if len(x) < 1:
            return "Invalid Triangle"
        else:
            values.update(x[0])
    else:
        values.update(x)
    for key, i in values.items():
        if not isinstance(i, int):
            values[key] = i.evalf(6)
    print(values)
    return values

    
    
 