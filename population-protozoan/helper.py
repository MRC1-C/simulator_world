import matplotlib.pyplot as plt
from config import BLOCK_SIZE, N_POPULATION, N_FOOD
from IPython import display

plt.ion()

def plot(plot,name):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    sum = []
    for i in range(len(plot[0])):
        s = 0
        for j in range(len(plot)):
            s+=plot[j][i]
        s = s/len(plot)
        sum.append(s)
    plt.xlabel('Number of days')
    plt.ylabel('en')
    for i in plot:
       plt.plot(i)
    plt.plot(sum, color="black")
    plt.ylim(ymin=0)
    plt.savefig("{}_{}_{}_{}".format(N_FOOD, N_POPULATION,BLOCK_SIZE, name))
    # plt.show()
