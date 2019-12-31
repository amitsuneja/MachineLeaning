import numpy as np
import matplotlib.pyplot as plt

"""
https://www.machinelearningplus.com/plots/matplotlib-tutorial-complete-guide-python-plot-examples/
"""

"""
A Basic Line
"""

plt.plot([1, 2, 3, 4, 10])
# plt.show()
plt.savefig("BasicLine.png")
plt.cla()  # Clear axis
plt.clf()  # Clear figure
plt.close()  # Close a figure window

"""
Basic Scatter Plot
"""
x = np.arange(5)
y = np.arange(5, 10)
plt.plot(x, y, 'go')
# plt.show()
plt.savefig("BasicScatter.png")
plt.cla()  # Clear axis
plt.clf()  # Clear figure
plt.close()  # Close a figure window


"""
 How to draw two sets of scatterplots in same plot
"""
StudentNumber = np.arange(5)
MarksInMaths = np.arange(5, 10)
MarksInPhysics = np.arange(5)
plt.figure(figsize=(10, 7))  # 10 is width, 7 is height
plt.plot(StudentNumber, MarksInMaths, 'ro', label="MarksInMaths")
plt.plot(StudentNumber, MarksInPhysics, 'go', label="MarksInPhysics")
plt.title('Marks in Maths and Physics for Each Student')
plt.xlabel('Student Number')
plt.ylabel('Marks Obtained')
plt.legend(loc='best')  # legend text comes from the plot's label parameter.
# plt.show()
plt.savefig("BasicScatterWith2Y.png")
plt.cla()  # Clear axis
plt.clf()  # Clear figure
plt.close()  # Close a figure window




"""
How to draw 2 scatterplots in different panels
"""

# Create Figure and Subplots
fig, (Maths_ax, Physics_ax) = plt.subplots(1, 2, figsize=(10, 4), sharey=False, dpi=120)
# Setting sharey=True in plt.subplots() shares the Y axis between the two subplots, Our y axis for both plots is
# different so we set it to False
# nd dpi=120 increased the number of dots per inch of the plot to make it look more sharp and clear.
# You will notice a distinct improvement in clarity on increasing the dpi
StudentNumber = np.arange(5)
MarksInMaths = np.arange(5, 10)
MarksInPhysics = np.arange(5)
Maths_ax.plot(StudentNumber, MarksInMaths, 'ro', label="MarksInMaths")
Physics_ax.plot(StudentNumber, MarksInPhysics, 'go', label="MarksInPhysics")
# Title, X and Y labels, X and Y Lim
Maths_ax.set_title('Marks in Maths for Each Student')
Physics_ax.set_title('Marks in Physics for Each Student')
Maths_ax.set_xlabel('Student Number');  Physics_ax.set_xlabel('Student Number')  # x label
Maths_ax.set_ylabel('Marks in Maths');  Physics_ax.set_ylabel('Marks in Physics')  # y label
Maths_ax.set_xlim(0, StudentNumber.max() + 1);  Physics_ax.set_xlim(0, StudentNumber.max() + 1)   # x axis limits
Maths_ax.set_ylim(0, MarksInMaths.max()+1);  Physics_ax.set_ylim(0, MarksInPhysics.max()+1)  # y axis limits
Physics_ax.legend(loc='best')
Maths_ax.legend(loc='best')
plt.tight_layout()
# plt.show()
plt.cla()  # Clear axis
plt.clf()  # Clear figure
plt.close()  # Close a figure window


"""
Draw multiple plots using for-loops using object oriented syntax
"""
np.random.seed(100)

# Create Figure and Subplots
fig, axes = plt.subplots(2,2, figsize=(15,8), sharex=False, sharey=False, dpi=120)

# Define the colors and markers to use
colors = {0:'g', 1:'b', 2:'r', 3:'y'}
markers = {0:'o', 1:'x', 2:'*', 3:'p'}
labels = {0:'Lab-1', 1:'Lab-2', 2:'Lab-3', 3:'Lab-4'}

# Plot each axes
for i, ax in enumerate(axes.ravel()):
    X = np.random.randint(0,10,10)
    Y = np.random.randint(0,10,10)
    ax.plot(sorted(X), sorted(Y), marker=markers[i], color=colors[i], label=labels[i])
    ax.legend(loc='best')
    # ax.yaxis.set_ticks_position('none')

plt.suptitle('Four Subplots in One Figure') #, verticalalignment='bottom', fontsize=16)
plt.tight_layout()
plt.show()
