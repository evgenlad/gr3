import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import func1
import func2
import func3
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
		self.f[self.n//2] += 0.5
		if self.ind == 0:
			ap = np.zeros(self.n)
			T = np.zeros(self.n)
			func1.coef(self.a, self.b, self.n, self.x, self.f, ap, T)
			(x1, y1) = func1.calc_given(self.a, self.b, self.n, ap)
		if self.ind == 1:
			ax.title.set_text('M.2')
			ap1 = np.zeros(self.n - 3)
			ap = np.array([ap1, ap1, ap1, ap1])
			func2.coef(self.n, self.x, self.f, ap)
			(x1, y1) = func2.calc_given(self.a, self.b, self.n, self.x, ap)
		if self.ind == 2:
			ax.title.set_text('M.3')
			ap1 = np.zeros(self.n - 3)
			ap = np.array([ap1, ap1, ap1, ap1])
			func3.coef(self.n, self.x, self.f, ap)
			(x1, y1) = func3.calc_given(self.a, self.b, self.n, self.x, ap)
		p.set_xdata(x1)
		p.set_ydata(y1)
		ax.title.set_text('Added delta +0.5, now f(x_{med}) = %f' % self.f[self.n//2])
		plt.draw()
	def deltam(self, event):
		self.f[self.n//2] -= 0.5
		if self.ind == 0:
			ap = np.zeros(self.n)
			T = np.zeros(self.n)
			func1.coef(self.a, self.b, self.n, self.x, self.f, ap, T)
			(x1, y1) = func1.calc_given(self.a, self.b, self.n, ap)
		if self.ind == 1:
			ax.title.set_text('M.2')
			ap1 = np.zeros(self.n - 3)
			ap = np.array([ap1, ap1, ap1, ap1])
			func2.coef(self.n, self.x, self.f, ap)
			(x1, y1) = func2.calc_given(self.a, self.b, self.n, self.x, ap)
		if self.ind == 2:
			ax.title.set_text('M.3')
			ap1 = np.zeros(self.n - 3)
			ap = np.array([ap1, ap1, ap1, ap1])
			func3.coef(self.n, self.x, self.f, ap)
			(x1, y1) = func3.calc_given(self.a, self.b, self.n, self.x, ap)
		p.set_xdata(x1)
		p.set_ydata(y1)
		ax.title.set_text('Substracted delta -0.5, now f(x_{med}) = %f' % self.f[self.n//2])
		plt.draw()
	def change(self, event):
		self.ind += 1
		self.ind = self.ind % 3
		x1 = np.array([0])
		y1 = np.array([0])
		if self.ind == 0:
			ax.title.set_text('M.1')
			loc_f = self.f[self.n//2]
			(self.x, self.f) = gfu.tf1(self.a, self.b, self.n)
			self.f[self.n // 2] = loc_f
			ap = np.zeros(self.n)
			T = np.zeros(self.n)
			func1.coef(self.a, self.b, self.n, self.x, self.f, ap, T)
			(x1, y1) = func1.calc_given(self.a, self.b, self.n, ap)
		if self.ind == 1:
			ax.title.set_text('M.2')
			loc_f = self.f[self.n//2]
			(self.x, self.f) = gfu.tf2(self.a, self.b, self.n)
			self.f[self.n // 2] = loc_f
			ap1 = np.zeros(self.n - 3)
			ap = np.array([ap1, ap1, ap1, ap1])
			func2.coef(self.n, self.x, self.f, ap)
			(x1, y1) = func2.calc_given(self.a, self.b, self.n, self.x, ap)
		if self.ind == 2:
			ax.title.set_text('M.3')
			loc_f = self.f[self.n//2]
			(self.x, self.f) = gfu.tf2(self.a, self.b, self.n)
			self.f[self.n // 2] = loc_f
			ap1 = np.zeros(self.n - 3)
			ap = np.array([ap1, ap1, ap1, ap1])
			func3.coef(self.n, self.x, self.f, ap)
			(x1, y1) = func3.calc_given(self.a, self.b, self.n, self.x, ap)
		#(x1, y1) = func1.calc_given(self.a, self.b, self.n, ap)
		p.set_xdata(x1)
		p.set_ydata(y1)
		#ax.title.set_text('Adjusted')
		plt.draw()
	def plus(self, event): #для текущего метода(если функция задана формулой) добавить точки
		self.n += 10
		if self.ind == 0:
			(self.x, self.f) = gfu.tf1(self.a, self.b, self.n)
			ap = np.zeros(self.n)
			T = np.zeros(self.n)
			func1.coef(self.a, self.b, self.n, self.x, self.f, ap, T)
			(x1, y1) = func1.calc_given(self.a, self.b, self.n, ap)
		if self.id == 1:
			(self.x, self.f) = gfu.tf2(self.a, self.b, self.n)
			ap1 = np.zeros(self.n - 3)
			ap = np.array([ap1, ap1, ap1, ap1])
			func2.coef(self.n, self.x, self.f, ap)
			(x1, y1) = func2.calc_given(self.a, self.b, self.n, self.x, ap)
		if self.id == 2:
			(self.x, self.f) = gfu.tf2(self.a, self.b, self.n)
			ap1 = np.zeros(self.n - 3)
			ap = np.array([ap1, ap1, ap1, ap1])
			func3.coef(self.n, self.x, self.f, ap)
			(x1, y1) = func3.calc_given(self.a, self.b, self.n, self.x, ap)
		p.set_xdata(x1)
		p.set_ydata(y1)
		ax.title.set_text('Added 10; n = %d' % self.n)
		plt.draw()
	def minus(self, event):
		if self.n < 11:
			return 0
		self.n -= 10
		if self.ind == 0:
			(self.x, self.f) = gfu.tf1(self.a, self.b, self.n)
			ap = np.zeros(self.n)
			T = np.zeros(self.n)
			func1.coef(self.a, self.b, self.n, self.x, self.f, ap, T)
			(x1, y1) = func1.calc_given(self.a, self.b, self.n, ap)
		if self.ind == 1:
			(self.x, self.f) = gfu.tf2(self.a, self.b, self.n)
			ap1 = np.zeros(self.n - 3)
			ap = np.array([ap1, ap1, ap1, ap1])
			func2.coef(self.n, self.x, self.f, ap)
			(x1, y1) = func2.calc_given(self.a, self.b, self.n, self.x, ap)
		if self.ind == 2:
			(self.x, self.f) = gfu.tf2(self.a, self.b, self.n)
			ap1 = np.zeros(self.n - 3)
			ap = np.array([ap1, ap1, ap1, ap1])
			func3.coef(self.n, self.x, self.f, ap)
			(x1, y1) = func3.calc_given(self.a, self.b, self.n, self.x, ap)
		p.set_xdata(x1)
		p.set_ydata(y1)
		ax.title.set_text('Substracted 10; n = %d' % self.n)
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
axdeltam = plt.axes([0.37, 0.05, 0.1, 0.075])

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

bdeltam = Button(axdeltam, 'deltam')
bdeltam.on_clicked(callback.deltam)

axButn1 = plt.axes([0.1, 0.1, 0.1, 0.1])
btn1 = Button(
axButn1, label="Home", color='pink', hovercolor='tomato')

#p1, = plt.plot(np.array([0]), np.array([0]), '^--b', linewidth=1.5, alpha=0.5)
def plot1(event):
	#ax.cla()
	#p, = plt.plot(x, f, '.--g', linewidth=2.5, alpha=0.8)
	#ax.title.set_text('Adjusted')
	#p1.remove()
	callback.x = x
	callback.f = f
	callback.n = n
	callback.a = a
	callback.b = b
	callback.id = id
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
	#plt.plot(callback.x, callback.f, '^--b', linewidth=1.5, alpha=0.5)

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