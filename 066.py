def pell_fundamental(n):
    x = int(n**0.5)
    y, z, r = x, 1, x*2
    e1, e2 = 1, 0
    f1, f2 = 0, 1
    
    while True:
        y = r*z - y
        z = (n - y**2)//z
        r = (x+y)//z
        e1, e2 = e2, e1 + e2*r
        f1, f2 = f2, f1 + f2*r
        a, b = f2*x + e2, f2
            
        if a**2 - n*b**2 == 1:
            return a, b


if __name__ == "__main__":
    x_max = 9
    D_max = 5

    for D in range(8, 1000+1):
        if int(D**0.5)**2 == D:
            continue
        else:
            tmp = pell_fundamental(D)
            
            if tmp[0] > x_max:
                x_max = tmp[0]
                D_max = D
                
    print(D_max)
