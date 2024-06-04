n = int(input("Enter the number of valueables = "))
m = int(input("Enter the number of condition = "))
z = input("enter the objective function is max or min : ")
C = list(map(int,input("enter C = ").split()))
A = []
for i in range(m):
    a = list(map(int,input(f'enter A{i+1} = ').split()))
    A.append(a)

B = list(map(int,input("enter B = ").split()))

sign_z = []
for i in range(1, m+1):
    s1 = input(f"enter sign of {i} condition : ")
    sign_z.append(s1)

sign_x = []    
for i in range(1, n+1):
    s2 = input(f"enter sign of x{i} : ")
    sign_x.append(s2)


if z == "max":
    print("min" ,end="  w = ")
elif z == "min":
    print("max" ,end="  w = ")  

At = []
for  i in range(n):
    A1 = []
    for j in range(m):
        A1.append(A[j][i])
    At.append(A1)

for i in range(m):
    print(B[i], end=f"y{i+1} ")
    if i == m-1:
        print("")
    else:    
        if B[i] >= 0 and B[i+1] >= 0:
            print(end="+")
        elif B[i] >= 0 and B[i+1] < 0:
            print(end="") 
        elif B[i] < 0 and B[i+1] < 0:
            print(end="")
        elif B[i] < 0 and B[i+1] >= 0:
            print(end="+")                   

Ap = []
for i in range(n):
    A1 = []
    for j in range(m):
        A1.append(A[j][i])
    Ap.append(A1)   

sign_y = []
for i in range(len(sign_z)):
    if z == "max":
        if sign_z[i] == "<=":
            sign_y.append(">=")  
        elif sign_z[i] == ">=":
            sign_y.append("<=")
        elif sign_z[i] == "=":
            sign_y.append("free")
    elif z == "min": 
        if sign_z[i] == ">=":
            sign_y.append(">=")  
        elif sign_z[i] == "<=":
            sign_y.append("<=")
        elif sign_z[i] == "=":
            sign_y.append("free")              

sign_w = []
for i in range(len(sign_x)):
    if z == "max":
        if sign_x[i] == "<=":
            sign_w.append("<=")
        elif sign_x[i] == ">=":
            sign_w.append(">=")
        elif sign_x[i] == "free":
            sign_w.append("=")     
    if z == "min":
        if sign_x[i] == ">=":
            sign_w.append("<=")
        elif sign_x[i] == "<=":
            sign_w.append(">=")
        elif sign_x[i] == "free":
            sign_w.append("=")   

print("s.t :")
for i in range(n):
    for j in range(m):
        print(format(Ap[i][j]),end=f"y{j+1} ")
        if j == n-1:
            print(end="")
        else:    
            if Ap[i][j] < 0 and Ap[i][j+1] >= 0:
                print(end="+") 
            elif Ap[i][j] < 0 and Ap[i][j+1] < 0:
                print(end="") 
            elif Ap[i][j] >= 0 and Ap[i][j+1] >= 0:
                print(end="+")
            elif Ap[i][j] >= 0 and Ap[i][j+1] < 0: 
                print(end="")     
    print(sign_w[i],C[i],"\n")    

for i in range(m):
    if sign_y[i] == "free":
        print(f"y{i+1} ",end=f"{sign_y[i]}\t ")
    else:    
        print(f"y{i+1} ",end=f"{sign_y[i]} {0} \t ")