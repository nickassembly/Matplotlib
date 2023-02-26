# basics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x = [0, 1, 2, 3, 4, 5]
# y = [0, 2, 4, 6, 8, 10]

# # resize graph
# # plt.figure(figsize=(5, 3), dpi=300) # use dpi of at least 300+ to avoid pixilated graph when zooming

# # Keyword argument Notation
# # plt.plot(x, y, label='2x', color='red', linewidth=2,
# #          marker='.', linestyle='--', markersize=10, markeredgecolor='blue')

# # shorthand
# # fmt = '[color] [marker][line]'
# plt.plot(x, y, 'b^--', label='2x')

# # Line 2
# # select interval to plot points at
# x2 = np.arange(0, 4.5, 0.5)

# # Plot part of the graph as line
# plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')

# # Plot remainder of graph as a dot
# plt.plot(x2[4:], x2[4:]**2, 'r--')

# # Add title (specify font params with fontdict KV pairs)
# plt.title('Keller graph', fontdict={
#           'fontname': 'Comic Sans MS', 'fontsize': 20})

# # X and Y Labels
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')

# # X and Y tick marks (scale of graph)
# plt.xticks([0, 1, 2, 3, 4])
# # plt.yticks([0, 2, 4, 6, 8, 10])

# # add legend to graph
# plt.legend()

# # save figure as file locally
# plt.savefig('mygraph.png', dpi=300)

# # show plotted graph
# plt.show()


# Bar Charts
# labels = ['A', 'B', 'C']
# values = [1, 4, 2]

# bars = plt.bar(labels, values)
# bars[0].set_hatch('/')
# bars[1].set_hatch('O')
# bars[2].set_hatch('*')


# plt.show()
