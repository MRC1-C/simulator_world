from environment import Environmaent
from agent import Agent
from agent_deep import Agent_D
from agent_rd import Agent_RD
from helper import plot
from config import N_POPULATION
from threading import Thread
def run(name, i):
    env = Environmaent(name + "_" +str(i))
    if name == "D":
        for id in range(N_POPULATION):
            new_agent = Agent_D(env,id)
            env.add_agent(new_agent)
    elif name == "Q":
        for id in range(N_POPULATION):
            new_agent = Agent(env,id)
            env.add_agent(new_agent)
    else:
        for id in range(N_POPULATION):
            new_agent = Agent_RD(env,id)
            env.add_agent(new_agent)
    while True:
        stop, n, sum_n,is_new_day = env.run()
        # if is_new_day:
        #     plot1.append(n)
        #     plot2.append(sum_n)
        #     plot(plot1, plot2)
        if stop:
            break

if __name__ == '__main__':
    t = ['RD','Q', 'D']
    # for i in range(10):
    #     t.append(Thread(target=run, args=(i,)))
    # for i in t:
    #     i.start()
    run('D',3)
    # for i in range(5,10):
    #     for j in t:
    #         run(j,i)
        # i.join()
    # for i in t:
        # i.start()
        # i.join()
        # t.join()
    # plot(plot1, plot2)
    # env.stop()