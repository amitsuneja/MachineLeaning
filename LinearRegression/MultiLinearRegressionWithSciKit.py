from sklearn.linear_model import LinearRegression
from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn import preprocessing


def create_boston_df():
    boston = datasets.load_boston()
    print(boston.keys())
    df = pd.DataFrame(data=boston.data, columns=boston.feature_names)
    df['target'] = boston.target
    my_dict = {"target": "Price"}
    df = df.rename(columns=my_dict)
    return df


df = create_boston_df()
ys = df['Price']
xs = np.c_[df['RM'], df['LSTAT'], ] # df['PTRATIO']]
print(ys.shape, xs.shape)  # if you check the shape of ys and xs vectors
# Data Standardizing
xs = preprocessing.scale(xs)
ys = preprocessing.scale(ys)
lm = LinearRegression()
lm = lm.fit(xs, ys)     # Fitting the model
pred = lm.predict(xs)   # This predicted vector will be of same size as of ys
print(pred.shape)
# We'll check the parameters from sci-kit learn
intercept = lm.intercept_
Theta_0 = lm.coef_[0]
Theta_1 = lm.coef_[1]
print('Intercept : {}'.format(round(intercept,3)))
print('Theta_0 : {}'.format(round(Theta_0,4)))
print('Theta_1 : {}'.format(round(Theta_1,4)))
r2_sk = lm.score(xs,ys)
print('R square from sci-kit learn: {}'.format(round(r2_sk,4)))
####################################################################



from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(12,10))
ax = Axes3D(fig)
ax.set_xlabel('Rooms', fontsize = 15)
ax.set_ylabel('Population', fontsize = 15)
ax.set_zlabel('Price', fontsize = 15)
plt.close()


def init():
    ax.scatter(xs[:, 0], xs[:, 1], ys, c='C6', marker='o', alpha=0.6)
    x0, x1 = np.meshgrid(xs[:, 0], xs[:, 1])
    yp = Theta_0 * x0 + Theta_1 * x1
    ax.plot_wireframe(x0, x1, yp, rcount=200, ccount=200, linewidth=0.5, color='C9', alpha=0.5)
    ax.legend(fontsize=15, labels=['Data points', 'Hyperplane'])
    return fig


def animate(i):
    ax.view_init(elev=10., azim=i)
    return fig


# Animate
my_ani = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20,
                                 blit=True)
my_ani.save('animation.gif', writer='pillow', fps=30)
plt.close()


