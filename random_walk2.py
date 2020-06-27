import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')


# randonly choose if the next step will be along the x, y or z axis

def probability1():
    x_y_z_direction = np.array([-1, 0, 1])
    probability = [1 / 3, 1 / 3, 1 / 3]
    direction = np.random.choice(a=x_y_z_direction, p=probability)
    return direction

# after choosing if the next step will be in the x, y, or z direction, choose if the next step will be in the positive or negative direction

def probability2():
    plus_minus_direction = np.array([-1, 1])
    probability = [0.5, 0.5]
    direction = np.random.choice(a=plus_minus_direction, p=probability)
    return direction

# set the x, y, and z coordinates of the next step

def random_walk(x, y, z):
    direction = probability1()
    if direction == 1:
        direction_x = probability2()
        x = x + direction_x
        return x, y, z
    elif direction == 0:
        direction_y = probability2()
        y = y + direction_y
        return x, y, z
    else:
        direction_z = probability2()
        z = z + direction_z
        return x, y, z
    return direction

# reshape the array to allow plot3D to use array

def reshape_array(old_array):
    new_array = np.array(old_array).reshape(n, )
    return new_array

# plot random walk

def plot_3D(x_array0, y_array0, z_array0, j):
    return ax.plot3D(x_array0, y_array0, z_array0, label='Random Walk #' + str(j + 1))



# def origin(n):
#     x0 = np.zeros(n, )
#     return x0


n = 1000
m = 3
x_array = np.zeros([n, m])
y_array = np.zeros([n, m])
z_array = np.zeros([n, m])


for j in range(m):
    x = 0
    y = 0
    z = 0
    for i in range(n):

        x_array[i, j] = x
        y_array[i, j] = y
        z_array[i, j] = z
        x, y, z = random_walk(x, y, z)

    x_array0 = reshape_array(x_array[:, j])
    y_array0 = reshape_array(y_array[:, j])
    z_array0 = reshape_array(z_array[:, j])
    plot_3D(x_array0, y_array0, z_array0, j)


ax.set_xlabel('x-direction')
ax.set_ylabel('y-direction')
ax.set_zlabel('z-direction')

ax.set_title('Three Random Walks\n 1000 Steps')

ax.legend(loc=(0.75, 0.9), frameon=0)

plt.show()
