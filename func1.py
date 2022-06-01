import numpy as np

def zox(a, b, x):
    if b != a:
        return 2*(2*x - (b + a))/(b - a)

def pol(a, b, n, x, ap):
    T = np.zeros(3)
    T[0] = 1
    z = zox(a, b, x)
    T[1] = z/2
    Pf = ap[0]*T[0] + ap[1]*T[1]
    for i in range(2, n):
        T[2] = z*T[1] - T[0]
        Pf += ap[i]*T[2]
        T[0] = T[1]
        T[1] = T[2]
    return Pf

def coef(a, b, n, x, f, ap, T):
    y = (x, f)
    np.sort(y, axis=0)
    for i in range(n):
        z = zox(a, b, x[i])
        for j in range(n):
            if j == 0:
                T[0] = 1
            if j == 1:
                T[1] = z/2
            if j > 1:
                T[j] = z*T[j - 1] - T[j - 2]
        ap += T*f[i]
    for i in range(n):
        if i == 0:
            ap[i] *= 1/n
        if i > 0:
            ap[i] *= 2/n

def calc_given(a, b, n, ap):
    x1 = np.linspace(a, b, 5 * n)
    y1 = np.zeros(5 * n)
    for i in range(5 * n):
        y1[i] = pol(a, b, n, x1[i], ap)
    return (x1, y1)



