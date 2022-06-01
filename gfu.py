import numpy as np

def f(x):
    return np.sin(x**2)

def tf0(name=''):
    file = open(name)
    data = file.read()
    data = list(map(float, data.split()))
    x = [data[0::2]]
    x = x[0]
    n = len(x)
    x = np.array(x)
    f = np.array([data[1::2]][0])
    file.close()
    return (x, f)

def tf1(a, b, n):
    #x = np.linspace(a + 1 / n, b - 1 / n, n)
    x = np.zeros(n)
    for m in range(n):
        x[m] = (a+b)/2 + ((b-a)/2)*np.cos(np.pi*(2*m-1)/(2*n))
    f1 = f(x)
    return (x, f1)
