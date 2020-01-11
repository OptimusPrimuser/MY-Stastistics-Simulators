import pandas as pd
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#upload data
data=pd.read_csv("scatter_plot_data.csv") #Simple linear regression.csv
#get x data
x=np.array(data.iloc[:,[0]])
x=np.reshape(x,len(x))
#to make it linear/reduce big nos to small nos e.g ** log base 10 of 100000000 = 8 **
x=np.log10(x)

max_x=max(x)
min_x=min(x)

#get y data
y=np.array(data.iloc[:,[1]])
y=np.reshape(y,len(y))
#to make it linear/reduce big nos to small nos e.g ** log base 10 of 100000000 = 8 **
y=np.log10(y)

#slope
m=0      
old_m=0 

#constant
c=0     
old_c=0
learning_rate=0.0001 #MAGNITUDE OF GRADIENT VECTOR

r_sqaure=2**64 #some high value

direction_factor=1 #changes the direction if goes in bad direction

#list of pervious slope,intercept,r square values
m_history=[]
c_history=[]
r_square_history=[]



#slope, intercept, r_square graph
fig_r_square=plt.figure()
ax_r_sqaure=plt.axes(projection='3d')
#naming everything
ax_r_sqaure.set_title("slope, intercept, r_square graph")
ax_r_sqaure.set_xlabel("m")
ax_r_sqaure.set_ylabel("c")
ax_r_sqaure.set_zlabel("r square")

#regression graph
fig_reg,ax_reg=plt.subplots()
#naming everything
ax_reg.set_xlabel("x")
ax_reg.set_ylabel("y")
ax_reg.set_title("regression graph")

#gradient graph
fig_gradient,ax_gradient=plt.subplots()
#naming everything
ax_gradient.set_xlabel("m")
ax_gradient.set_ylabel("c")
ax_gradient.set_title("gradient graph")
#method called when mouse is clicked in gradient graph 🤙🤙🤙🤙
def getPoint_from_gradient_graph(event):
    global min_x
    global max_x
    m=event.xdata
    c=event.ydata

    #clear data from regression graph
    ax_reg.clear()
    ax_reg.plot( [min_x,max_x], [(m*min_x)+c,(m*max_x)+c] )
    
    #ploting data 📈📈📈 on regression graph
    ax_reg.scatter(x,y)
    
    #drawing regression line when co ordinate is clicked in gradient graph
    plt.draw_all()

#connecting mouse to gradient graph to make regression line on regression graph
fig_gradient.canvas.mpl_connect('button_press_event', getPoint_from_gradient_graph)



#gets the line of regression
def gradientPlot():
    #used to tell function that we are using outside variables(global variables 🤷‍♂)
    global m
    global old_m
    global c
    global old_c
    global r_sqaure
    global direction_factor
    global m_history
    global c_history

    #used to check if we are minimising average of r square or not 
    #if not used this function will reach heights 🔝🔝🔝
    temp_val_for_r_square=0
    #makes a predicted value numpy array
    y_predicted=m*x+c
    
    #difference between actual and predicted value 
    error=(y_predicted-y)
    direction=2*error*learning_rate*direction_factor
    
    #calculating average of r square(coefficient of determination 🤔)
    temp_val_for_r_square=error**2
    temp_val_for_r_square=temp_val_for_r_square.sum()/len(temp_val_for_r_square)
    
    #if r square value is not minimised then take reverse gear(reverse direction 😑)
    #else continue on your path 🏃‍♂🏃‍♂🏃‍♂🏃‍♂
    if(temp_val_for_r_square>r_sqaure):
        direction_factor=direction_factor*(-1)
        m=old_m
        c=old_c
        return
    else:
        r_sqaure=temp_val_for_r_square
        old_m=m
        old_c=c

    #changing values of m and averaging them
    m=m-(x*direction)
    m=m.sum()/len(m)
    #changing values of c and averaging them 😪
    c=c-(direction)
    c=c.sum()/len(c)

    #keeping history records📚📚(keeping the values of m,c,r_square for graph)
    m_history.append(m)
    c_history.append(c)
    r_square_history.append(r_sqaure)
    

#runing the gradient finding funtion 100000 times (🚂🚂🚂🚂🚂) 
for i in range(100000):
    gradientPlot()

#ploting data 📈📈📈 on regression graph
ax_reg.scatter(x,y)

#plotting all the values of slope and intercept on gradient plot
ax_gradient.plot(m_history,c_history)

#plotting all the values of slope, intercept and r_square on gradient plot
ax_r_sqaure.plot(m_history,c_history,r_square_history)

#show me the goods amigo!🦸‍♂🦸‍♂ (all graph)
plt.show()
