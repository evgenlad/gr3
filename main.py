import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import func1
import gfu

class graph:
	id = 0
	ind = 0
	a = 0
	b = 0
	n = 1
	x = []
	f = []
	def delta(self, event):
		ap = np.zeros(self.n)
		T = np.zeros(self.n)
		self.f[self.n//2] += 0.5
		if self.ind == 0:
			func1.coef(self.a, self.b, self.n, self.x, self.f, ap, T)
		(x1, y1) = func1.calc_given(self.a, self.b, self.n, ap)
		p.set_xdata(x1)
		p.set_ydata(y1)
		ax.title.set_text('Adjusted')
		plt.draw()
	def change(self, event):
		self.ind += 1
		self.ind = self.ind % 3
		ap = np.zeros(self.n)
		T = np.zeros(self.n)
		if self.ind == 0:
			func1.coef(self.a, self.b, self.n, self.x, self.f, ap, T)
		(x1, y1) = func1.calc_given(self.a, self.b, self.n, ap)
		p.set_xdata(x1)
		p.set_ydata(y1)
		ax.title.set_text('Adjusted')
		plt.draw()
	def plus(self, event): #для текущего метода(если функция задана формулой) добавить точки
		self.n += 10
		(self.x, self.f) = gfu.tf1(self.a, self.b, self.n)
		ap = np.zeros(self.n)
		T = np.zeros(self.n)
		if self.ind == 0:
			func1.coef(self.a, self.b, self.n, self.x, self.f, ap, T)
		(x1, y1) = func1.calc_given(self.a, self.b, self.n, ap)
		p.set_xdata(x1)
		p.set_ydata(y1)
		ax.title.set_text('Adjusted')
		plt.draw()
	def minus(self, event):
		if self.n < 11:
			return 0
		self.n -= 10
		(self.x, self.f) = gfu.tf1(self.a, self.b, self.n)
		ap = np.zeros(self.n)
		T = np.zeros(self.n)
		if self.ind == 0:
			func1.coef(self.a, self.b, self.n, self.x, self.f, ap, T)
		(x1, y1) = func1.calc_given(self.a, self.b, self.n, ap)
		p.set_xdata(x1)
		p.set_ydata(y1)
		ax.title.set_text('Adjusted')
		plt.draw()

print('a')
a = float(input())
print('b')
b = float(input())
print('id: 0 -- from file, 1 -- given')
id = int(input())
x = []
if id == 0:
	(x, f) = gfu.tf0('a.dat')
if id == 1:
	print('n')
	n = int(input())
	(x, f) = gfu.tf1(a, b, n)
#ap = np.zeros(n)
#T = np.zeros(n)

#func1.coef(a, b, n, x, f, ap, T)
#(x1, y1) = func1.calc_given(a, b, n, ap)
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)
p, = plt.plot(x, f, '.--g', linewidth=2.5, alpha=0.8)
ax.title.set_text('Adjusted')

axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
axdrev = plt.axes([0.59, 0.05, 0.1, 0.075])
axdelta = plt.axes([0.48, 0.05, 0.1, 0.075])

callback = graph()
callback.x = x
callback.f = f
callback.n = n
callback.a = a
callback.b = b
callback.id = id

bnext = Button(axnext, 'Change')
bnext.on_clicked(callback.change)
if id == 1:
	bprev = Button(axprev, 'plus10')
	bprev.on_clicked(callback.plus)
	bdrev = Button(axdrev, 'minus10')
	bdrev.on_clicked(callback.minus)
bdelta = Button(axdelta, 'delta')
bdelta.on_clicked(callback.delta)

axButn1 = plt.axes([0.1, 0.1, 0.1, 0.1])
btn1 = Button(
axButn1, label="Home", color='pink', hovercolor='tomato')

def plot1(event):
	p.set_xdata(x)
	p.set_ydata(f)
	ax.title.set_text('Given linear')
	plt.draw()

btn1.on_clicked(plot1)

axButn2 = plt.axes([0.3, 0.1, 0.1, 0.1])
btn2 = Button(
axButn2, label="Both", color='pink', hovercolor='tomato')

def plot2(event):
	#p.set_xdata(x)
	#p.set_ydata(f)
	ax.title.set_text('Adjusted')
	ax.plot(callback.x, callback.f, color="blue", marker="^")
btn2.on_clicked(plot2)

#axButn3 = plt.axes([0.5, 0.1, 0.1, 0.1])
#btn3 = Button(
#axButn3, label="D", color='pink', hovercolor='tomato')

#def plot3(event):
#	p.set_xdata(x)
#	p.set_ydata(f)
#	ax.title.set_text('Given linear')
#	plt.draw()
#
#btn2.on_clicked(plot3)
plt.show()