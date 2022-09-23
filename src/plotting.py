import matplotlib.pyplot as plt

def get_avg(data: list[tuple[float, float]]) -> tuple[float, float]:
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    return (round(sum(x)/len(x), 2), round(sum(y)/len(y), 2))


def get_delta(avg: list[float, float],
              datapoint: list[float, float]
              ) -> tuple[float, float]:
    return (round(datapoint[0]-avg[0], 2), round(datapoint[1]-avg[1], 2))


def plot_data(figure, data: list[list[float, float]], outliers: list) -> object:
    x = [i[0] for i in data]
    y = [i[1] for i in data]
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
    plt.ylim([-5, 5])
    plt.xlim([-5, 5])
    plt.scatter(x, y, color="green")
    plt.scatter(outliers_x, outliers_y, color="red")

    centers = get_avg(data)
    # # compute radius
    # r = np.sqrt((np.array(x) - centers[0])**2 + (np.array(y) - centers[1])**2)
    # t = 10 # percent
    # r0 = np.percentile(r, t)
    # print(f'r={r}\nt={t}\nr0={r0}')

    # circle = plt.Circle((centers[0], centers[1]), r0, color='r', fill=False)
    # plt.gca().add_artist(circle)

    # plt.scatter(centers[0], centers[1], color = 'blue', marker = 'o', s = 8000, alpha = 0.1)
    plt.scatter(centers[0], centers[1], color='k', marker='x', s=50)

    return figure


# fig = plt.figure(num=1, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')

# data = [[-0.7, -0.5], [0.4, -0.7], [0.6, 0.09], [-0.1, 0.6], [0.4, -0.2], [-3.6, 3.9]]
# data = [(-0.7, -0.5), (0.6, -0.9), (0.8, 1.0)]

# outliers = get_outliers(data)

# my_plot = plot_data(fig, data, outliers)
# data_2 = [(3.0, 2.4), (2.8, 2.0), (3.2, 2.1)]
# avg_2 = avg(data_2)
# new_plot = plot_data(fig, new_data)

# plt.show()
