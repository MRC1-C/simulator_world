import numpy as np
n_state = 8
n_action = 3
getbinary = lambda x: format(x, 'b').zfill(n_state)
getdecimal = lambda x:int(x,2) 
q_table = np.random.uniform(low=-2, high=0, size=(n_state, n_action))

def index_to_state(x):
    x = format(int(x), 'b').zfill(n_state)
    state = []
    for i in x: 
        state.append(int(i))
    return np.array(state) 


def get_action(state):
    index = np.argmax(state)
    if index == 0:
        return np.array([1,0,0])
    elif index == 1:
        return np.array([0,1,0])
    else: 
        return np.array([0,0,1])


test = [[1,0],[0,0]] 
import numpy as np

arr = np.array([1,2,3,4,5,6])
arr1 = arr
arr1[0] = 40
print(arr)
print(arr1)