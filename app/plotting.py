'''This module is for development and testing purposes only'''
import matplotlib.pyplot as plt
from grouping import Group
import numpy as np


def get_avg(data: list[tuple[float, float]]) -> tuple[float, float]:
    x, y = [i[0] for i in data], [i[1] for i in data]
    return (round(sum(x)/len(x), 2), round(sum(y)/len(y), 2))


def get_median(data: list[tuple[float, float]]) -> tuple[float, float]:
    x, y = np.array([i[0] for i in data]), np.array([i[1] for i in data])
    return (np.median(x), np.median(y))


def get_std(data: list[tuple[float, float]]) -> tuple[float, float]:
    x, y = np.array([i[0] for i in data]), np.array([i[1] for i in data])
    return (np.std(x), np.std(y))


def get_delta(avg: list[float, float],
              datapoint: list[float, float]
              ) -> tuple[float, float]:
    return (round(datapoint[0]-avg[0], 2), round(datapoint[1]-avg[1], 2))


def plot_data(figure, data: list[list[float, float]], outliers: list = None) -> object:
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    if outliers is not None:
        outliers_x, outliers_y = [x[i] for i in outliers], [y[i] for i in outliers]

    plt.style.use('bmh')
    plt.rcParams.update({'font.size': 18})

    plt.xlabel('x')
    plt.ylabel('y')
    plt.minorticks_on()

    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle='-', linewidth='0.5', color='black')

    plt.axhline()
    plt.axvline()
    
    plt.ylim([-25, 25])
    plt.xlim([-25, 25])
    plt.scatter(x, y, color="green")
    if outliers is not None:
        plt.scatter(outliers_x, outliers_y, color="red")

    centers = get_avg(data)
    median = get_median(data)
    std = get_std(data)
    # compute radius
    r = np.sqrt((np.array(x) - median[0])**2 + (np.array(y) - median[1])**2)
    t = std[0]+std[1] / len(std)  # percent?
    # t = 10
    r0_2 = np.percentile(r, t)
    r0 = np.percentile(r, t)
    print(f'r={r}\nt={t}\nr0={r0}')

    circle2 = plt.Circle((median[0], median[1]), r0_2, color='green', fill=False)
    circle = plt.Circle((median[0], median[1]), r0, color='r', fill=False)
    plt.gca().add_artist(circle)
    plt.gca().add_artist(circle2)

    # plt.scatter(centers[0], centers[1], color = 'blue', marker = 'o', s = 8000, alpha = 0.1)
    plt.scatter(centers[0], centers[1], color='k', marker='x', s=50)
    plt.scatter(median[0], median[1], color='red', marker='x', s=50)

    return figure


fig = plt.figure(num=1, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')

data = [[-7, -5], [4, -7], [6, 9], [-1, 6], [4, -2], [-24, 20]]
# data = [(-0.7, -0.5), (0.6, -0.9), (0.8, 1.0)]

group = Group(data)

my_plot = plot_data(fig, group.shots)
# data_2 = [(3.0, 2.4), (2.8, 2.0), (3.2, 2.1)]
# avg_2 = avg(data_2)
# new_plot = plot_data(fig, new_data)

plt.show()
