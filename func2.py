import numpy as np

#Схема: считаются коэффициенты d_i -> коэффициенты c1_i, .., c4_i, 2...i...n-1.
#Значени восстанавливается пт схеме: в зависимости от расположения x - f(x) - многочлен с нужными коэффициентами
#Причем P_1 = P_2, P_{n-1} = P_n

def pol(a, b, n, x, x0, ap):
    for i in range(n-1):
        if x0 <= x[i+1] and x0 >= x[i] :
            f = i
            break
    if (i+1)> 1 and (i+1)<(n-1):
        return (ap[0][i-1] + ap[1][i-1]*(x0-x[i]) + ap[2][i-1]*((x0-x[i])**2) + ap[3][i-1]*((x0-x[i])**3))
    if i == 0:
        return (ap[0][0] + ap[1][0] * (x0 - x[i]) + ap[2][0] * ((x0 - x[i]) ** 2) + ap[3][0] * (
                    (x0 - x[i]) ** 3))
    if i ==  (n-2):
        return (ap[0][n-3] + ap[1][n-3] * (x0 - x[i]) + ap[2][n-3] * ((x0 - x[i]) ** 2) + ap[3][n-3] * (
                (x0 - x[i]) ** 3))

def coef(n, x, f, ap):
    df = np.zeros(n-1) #df[i] = f(x_i; x_{i+1})
    dx = np.zeros(n-1)
    print("1-n",x[1:n])
    print("0, n-1",x[0:(n-1)])
    dx = x[1:n] - x[0:(n-1)]
    print(x)
    print(dx)
    df = (f[1:n] - f[0:(n-1)])/(x[1:n] - x[0:(n-1)])
    d = np.zeros(n-2) # d[0] = d_2
    d = (dx[1:(n-1)]*df[0:(n-2)] + dx[0:(n-2)]*df[1:(n-1)])/(dx[1:(n-1)] + dx[0:(n-2)])
    #ck_2 = c[0]
    c1 = np.zeros(n-3)
    c2 = np.zeros(n-3)
    c3 = np.zeros(n-3)
    c4 = np.zeros(n-3)
    c1 = f[1:(n-3)]
    c2 = d[0:(n-3)]
    c3 = (3*df[1:(n-2)] - 2*d[0:(n-3)] - d[1:(n-2)])/dx[1:(n-2)]
    c4 = (d[0:(n-3)] - d[1:(n-2)] - 2*df[1:(n-2)])/(x[1:(n-2)]**2)
    ap[0] = c1
    ap[1] = c2
    ap[2] = c3
    ap[3] = c4

def calc_given(a, b, n, x, ap):
    x1 = np.linspace(a, b, 5 * n)
    y1 = np.zeros(5 * n)
    for i in range(5 * n):
        y1[i] = pol(a, b, n, x, x1[i], ap)
    return (x1, y1)
