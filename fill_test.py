import matplotlib.pyplot as plt

# input_values=[1,2,3,4,5]
# squares=[1,4,9,16,25]
# plt.plot(input_values,squares,linewidth=3)
# plt.title("Square Numbers",fontsize=18)
# plt.xlabel("Value",fontsize=15)
# plt.ylabel("Square of Value",fontsize=15)
# plt.tick_params(axis='both',labelsize=15)
#
# # plt.show()
#
# x_values=list(range(1,100))
# y_values=[x**2 for x in x_values]
# plt.scatter(x_values,y_values,c='green',edgecolors=None,s=40)
# plt.title("Square numbers",fontsize=22)
# plt.xlabel("value",fontsize=12)
# plt.ylabel("square value",fontsize=11)
#
# plt.tick_params(axis='both',which='major',labelsize=5)
# plt.savefig('squart_plot.png',bbox_inches='tight')
# plt.axis([0,100,0,10000])
# plt.show()
from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self,num_points=5000):

        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):

        while (len(self.x_values)<self.num_points):

            x_step=self.get_step()
            y_step=self.get_step()


            if x_step ==0 and y_step==0:
                continue

            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        z_direction = choice([1, -1])
        z_distance = choice([0, 1, 2, 3, 4])
        walk = z_direction * z_distance
        return walk





