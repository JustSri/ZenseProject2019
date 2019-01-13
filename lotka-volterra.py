import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as graph
from Tkinter import *
#Initial Selection Screen Of Factors
Select_Screen = Tk(className='Factors In The Simulation')
#Text Describing the Simulation
name = Label(Select_Screen,text='The Lotka-Volterra model for the population of a predator and prey species in a given environment is a set of two differential equations that calculates their populations given certain factors')
name.pack()
name1 = Label(Select_Screen,text='There are certain assumptions this model makes:')
name1.pack()
name2 = Label(Select_Screen,text='1.The prey species finds sufficient amount of food at all times')
name2.pack()
name3 = Label(Select_Screen,text='2.The food supply of the predator species depends solely on the prey population')
name3.pack()
name4 = Label(Select_Screen,text='3.The rate of change of population is proportional to its size')
name4.pack()
name5 = Label(Select_Screen,text='4.During the process,the enviroment doesn\'t change in favour of any species, and genetic adaptation doesn\'t affect anything')
name5.pack()
name6 = Label(Select_Screen,text='5.Predator have limitless appetite')
name6.pack()
name7 = Label(Select_Screen,text='')
name7.pack()
name8 = Label(Select_Screen,text='Please select the initial populations and the various constants you would like in your graph, then close this Window to be able to select the graph')
name8.pack()
name10 = Label(Select_Screen,text='Alpha represents the rate of growth of the population of the prey species in the absence of predators, affected by eg. the relative prevalence of food or water supply for the prey species')
name10.pack()
name11 = Label(Select_Screen,text='Beta represents the rate for the Prey of encountering the Predator(and thus dying), affected by eg. the landmass which would increase the chance of the predator and prey species meeting')
name11.pack()
name12 = Label(Select_Screen,text='Delta represents the rate for the Predator of encountering the Prey(the Predator\'s food), affected by eg. the landmass which would increase the chance of the predator and prey species meeting')
name12.pack()
name13 = Label(Select_Screen,text='Gamma represents the rate of population decrease for the predator in the absence of any prey species, affected by eg. the water supply, natural death rate or emigration rate for the predator species')
name13.pack()
name14 = Label(Select_Screen,text='')
name14.pack()
#Button Sliders For The Values
values = []
prey_init = Scale(Select_Screen,from_=0,to=10,length=500,orient=HORIZONTAL,label='Initial Population of the Prey')
prey_init.pack()
predator_init = Scale(Select_Screen,from_=0,to=10,length=500,orient=HORIZONTAL,label='Initial Population of the Predator')
predator_init.pack()
alpha = Scale(Select_Screen,from_=0,to=100,length=500,orient=HORIZONTAL,label='Alpha *  100')
alpha.pack()
beta = Scale(Select_Screen,from_=0,to=100,length=500,orient=HORIZONTAL,label='Beta *  100')
beta.pack()
delta = Scale(Select_Screen,from_=0,to=100,length=500,orient=HORIZONTAL,label='Delta * 100')
delta.pack()
gamma = Scale(Select_Screen,from_=0,to=100,length=500,orient=HORIZONTAL,label='Gamma * 100')
gamma.pack()
def store_values():
    if values == []:
        values.append(prey_init.get())
        values.append(predator_init.get())
        values.append(alpha.get()/100.0)
        values.append(beta.get()/100.0)
        values.append(delta.get()/100.0)
        values.append(gamma.get()/100.0)
    else:
        values[0] = (prey_init.get())
        values[1] = (predator_init.get())
        values[2] = (alpha.get()/100.0)
        values[3] = (beta.get()/100.0)
        values[4] = (delta.get()/100.0)
        values[5] = (gamma.get()/100.0)
Button(Select_Screen,text='Use These Factors',command=store_values).pack()
mainloop()
#Buttons For The Options of Simulation
Simulation = Tk(className='The Actual Simulation')
name = Label(Simulation,text='Select whether you want to see a Population vs Time graph for both species or a Predator vs Prey population graph(known as a phase space diagram)\nPlease close the window once you have selected your graph type')
name.pack()
graph_type = []
def population_graph():
    if graph_type == []:
        graph_type.append('population')
def phase_graph():
    if graph_type == []:
        graph_type.append('phase')
Button(Simulation,text='Population Graph',command=population_graph).pack()
Button(Simulation,text='Phase Space Diagram',command=phase_graph).pack()
mainloop()
#Graphing Part
a = values[2]
b = values[3]
d = values[4] 
c = values[5]
def pop_model(population,time):
    [prey,predator] = population
    return [(a*prey-b*prey*predator),(d*prey*predator-c*predator)]
pop_init = [values[0],values[1]]
time = np.linspace(0,20,1000)
solution = integrate.odeint(pop_model,pop_init,time)
prey = []
predator = []
for i in solution:
    prey.append(i[0])
    predator.append(i[1])
#Population Graph
if graph_type[0] == 'population':
    graph.xlim(0,20)
    graph.ylim(0,20)
    graph.plot(time,prey,color='blue',label='Prey')
    graph.plot(time,predator,color='red',label='Predator')
    graph.grid()
    graph.legend(loc='best')
    graph.xlabel('Time')
    graph.ylabel('Population')
    graph.title('Lotka-Volterra Equations')
    graph.show()
#Phase Graph
if graph_type[0] == 'phase':
    graph.xlim(0,20)
    graph.ylim(0,20)
    graph.plot(prey,predator,color='green')
    graph.grid()
    graph.xlabel('Prey')
    graph.ylabel('Predator')
    graph.title('Lotka-Volterra Equations Part 2')
    graph.show()
