import matplotlib.pyplot as plt
import numpy as np

def avg(data: list[float]) -> float:
    return sum(data)/len(data) 

def plot_data(figure, data: list[tuple[float, float]]) -> object:
    data = data

    x = [i[0] for i in data]
    y = [i[1] for i in data]

    plt.style.use('bmh')
    plt.rcParams.update({'font.size':18})

    plt.xlabel('x')
    plt.ylabel('y')
    plt.minorticks_on()

    plt.grid(which='major', linestyle='-' ,linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle='-' ,linewidth='0.5', color='black')

    plt.axhline()
    plt.axvline()
    plt.ylim([-5, 5])
    plt.xlim([-5, 5])
    plt.scatter(x,y, color="green")

    # print(avg(x))
    centers_x = avg(x)
    centers_y = avg(y)
    
    # # compute radius
    # r = np.sqrt((np.array(x) - centers_x)**2 + (np.array(y) - centers_y)**2)
    # t = 10 # percent
    # r0 = np.percentile(r, t)

    # print(f'r={r}\nt={t}\nr0={r0}')

    # circle = plt.Circle((centers_x, centers_y), r0, color='r', fill=False)
    # plt.gca().add_artist(circle)

    # plt.scatter(centers_x, centers_y, color = 'blue', marker = 'o', s = 8000, alpha = 0.1)
    plt.scatter(centers_x, centers_y, color = 'k', marker = 'x', s = 50)

    return figure


fig = plt.figure(num=1, figsize=(10,10),dpi=80, facecolor='w', edgecolor='k')


# generate some random points
# n = 1000
# x = 4 * np.random.randn(n) + 15
# y = 2 * np.random.randn(n) + 10


data = [(1.0,2.0),(1.5, 2.2),(1.3, 2.1),(-3.0,2.0),(0.0,1.8),(-1.0,-1.0)]
my_plot = plot_data(fig, data)

new_data = [(3.0,2.4),(2.8, 2.0),(3.2, 2.1)]
new_plot = plot_data(fig, new_data)

plt.show()