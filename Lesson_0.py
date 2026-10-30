from matplotlib import pyplot as plt
import gymnasium as gym


x = [1,2,3,4,5]
y = [4,5,6,7,8]

#plt.plot(x,y)
#plt.show()

env = gym.make('CartPole-v1')
state = env.reset()

print(state)
print(x)