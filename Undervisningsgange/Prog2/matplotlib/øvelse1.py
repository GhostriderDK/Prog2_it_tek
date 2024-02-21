import matplotlib.pyplot as plt
import numpy as np

x1points = np.array([0, 2, 4, 6, 8, 10, 12, 14])
y1points = np.array([0, 2, 8, 10, 4, 2, 9, 4])
y2points = np.array([0, 8, 1, 3, 0, 10, 5, 4])

fig, ax = plt.subplots()

ax.set_facecolor("#000")
fig.patch.set_facecolor('#250127') # outer plot background color HTML

ax.plot(x1points, y2points, linestyle = 'dotted', c = '#c800ff', linewidth = '2.0',
    marker = 'D', mec = 'yellow', ms = 10, mfc = 'yellow' )
ax.plot(x1points, y1points, linestyle = 'dashed', c = '#ffff', linewidth = '1.5',
    marker = '*', mec = 'red', ms = 10, mfc = 'white' )

ax.set_xlabel('X-axis ')
ax.set_ylabel('Y-axis ')

ax.xaxis.label.set_color('red') #setting up X-axis label color to hotpink
ax.yaxis.label.set_color('Yellow') #setting up y-axis label color to hotpink

ax.tick_params(axis='x', colors='red')
ax.tick_params(axis='y', colors='yellow')

ax.spines['left'].set_color('white') # setting up Y-axis tick color to blue
ax.spines['top'].set_color('purple') #setting up above X-axis tick color to blue
ax.spines['bottom'].set_color('white') #setting up above X-axis tick color to blue
ax.spines['right'].set_color('purple') #setting up above X-axis tick color to blue

plt.show()