import matplotlib.pyplot as plt

from Test.fill_test import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.figure(figsize=(10,8))
    point_numbers=list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=10)

    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n)")

    if keep_running == 'n':
        break


