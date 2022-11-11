# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 22:43:49 2022

@author: Huawei
"""
import pandas as pd
import matplotlib.pyplot as plt
 
data=pd.read_excel("suicideratedata.xlsx") #Reading data from excel file  
print(data)
data_drop=data.drop(["Location","Both sexes"], axis=1) #dropping columns not required for line plot
print(data_drop)
new_data=data_drop.head()                              #selecting the first 5 rows
print(new_data)
period= new_data["Period"].astype(str)                 #Converting column dtype float to string 

def line_plot(x_axis, y_axis, name, colors):           #defining function for line plot with arguments
    plt.plot(x_axis,y_axis,label=name,color=colors)    
plt.figure(dpi=144)                                    #resolution and clarity purpose of graph
line_plot(period, new_data["Male"],"Male","yellow")    #calling function to plot line
line_plot(period, new_data["Female"],"Female","blue")
plt.xlabel("Years")
plt.ylabel("Category")
plt.title("Age-specific Suicide rates")
plt.legend(loc="best")                                 #at the best location it will display the legend
plt.savefig("Line_Plot.png")
plt.show()
    
#dropping Columns location,Male,Female which is not required for pie chart
col_drop=data.drop(["Location","Male","Female"], axis=1)  
print(col_drop)
new_values=col_drop.head()      
print(new_data)
data_both=new_values["Both sexes"]
period=new_values["Period"]

def pie_plot(label,values):                            #defining function for pie plot with arguments
    plt.figure(dpi=144)
    colors = ['yellowgreen', 'red', 'violet', 'lightskyblue', 
          'cyan']
    plt.pie(values, labels=label,colors=colors, startangle=90,radius=1.2,autopct="%1.1f%%",pctdistance=0.5,labeldistance=1.1)
    plt.title("Suicide Rate of Both Sexes(2015-2019)")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig("Pie_Chart.png")
    plt.show() 
pie_plot(period,data_both)

def bar_plot(genre_data):                              #defining function for bar plot with arguments
    #Reading data from csv file for bar plot
    plt.figure(dpi=144)
    colors = ['yellowgreen', 'red', 'lightskyblue',       
              'cyan','lightcoral','blue','pink', 'darkgreen', 
              'yellow','grey','violet','magenta']
    #bar_plot(genre_data["genre"],genre_data["sales"])
    plt.xticks(rotation=90)
    plt.xlabel("Genre")
    plt.ylabel("Sales")
    plt.bar(genre_data["genre"],genre_data["sales"],color=colors)
    plt.title("Total Video Games from 1980-2000")
    plt.savefig("Bar_Plot.png")
    plt.show()
genre_data=pd.read_csv("genre_totals.csv")
bar_plot(genre_data)