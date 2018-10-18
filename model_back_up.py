import matplotlib.pyplot
import operator    
import random
num_of_agents = 10
agents=[]
for i in range(num_of_agents):
	agents.append([random.randint(0,100),random.randint(0,100)]) # add random generated coordinates to the list

#y1=random.randint(0,99)
#x1=random.randint(0,99)
#agents.append([y1,x1])
print(agents)
print(max(agents))
print(max(agents, key=operator.itemgetter(1)))    
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()

x=0
y=0
agents=[]
num_of_agents=100
for i in range(num_of_agents):
	if random.random() < 0.5:
		x+=1
		y+=1
	else:
		x-=1
		y-=1
	i+=1
	agents.append([y,x])
print(agents)

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()	
	
