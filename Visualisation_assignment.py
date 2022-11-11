# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 22:05:03 2022
@author: Ayush Jha
Assignment : Visualisation
"""

#All imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to get the data using year and column name
def getDataByYrandCol(year,colName): 
   '''Geting the data using particular
   column name and year'''
   #Reading Data from the excel
   emp_data = pd.read_excel('Finaldata.xlsx')
   #Setting index 
   emp_data.set_index("Year", inplace = True)
   result = emp_data.loc[[year],[colName]]
   return result.iloc[0].iloc[0]

# Function to get the colour of bar using column name
def getColumnColor(value): 
   '''Fetching the color of each bar besad on the column name'''
   col = []
   for val in value:
       if val == "Female(2007)":
           col.append('Hotpink')
       elif val == "Female(2016)":
           col.append('Hotpink')
       elif val == "Male(2007)":
           col.append('Blue')
       else:
           col.append('Blue')          
   return col

#function to get the number of person using percentage
def getNumberofperson(x,y): 
   '''Fetching the number of person using percentage'''
   value = (x * y)/100
   return value

# function to find the percentage
def getpPercentage(x,y): 
   '''Fetching the percentage using values'''
   percentage = (x/y)*100
   return percentage
      
#Reading Data from the excel
emp_data = pd.read_excel('Finaldata.xlsx')

#plot graph
#setting figure size
plt.figure(figsize=(10,8))
plt.title('Employement data by sector for UK(2007-2016)')
plt.plot(emp_data["Year"],emp_data["agriculture(%)"],label="Agriculture")
plt.plot(emp_data["Year"],emp_data["industry(%)"],label="Industry")
plt.plot(emp_data["Year"],emp_data["services(%)"],label="Service")
plt.xlabel("Year")
plt.ylabel("Employment by sectors(%)")
plt.yticks(np.arange(0, 100, 5))
plt.xticks(np.arange(2007, 2017, 1))
plt.legend()
plt.show()

#Getting data using the function getDataByYrandCol
service_Female2007 = getDataByYrandCol(2007,"services, female(%)")
service_Female2016 = getDataByYrandCol(2016,"services, female(%)")
service_Male2007 = getDataByYrandCol(2007,"services, male (%)")
service_Male2016 = getDataByYrandCol(2016,"services, male (%)")

#Bar graph 
plt.figure(figsize=(10,10))
genderWithYear= np.array(["Female(2007)","Female(2016)","Male(2007)","Male(2016)"])
empPercentage=np.array([service_Female2007,service_Female2016,service_Male2007,service_Male2016])
#Setting up color besad on gender
col = getColumnColor(genderWithYear)
plt.ylabel("Employement in percentage")   
plt.title('Change in gender participation in service sector(uk) between 2007 and 2016 in %')
plt.yticks(np.arange(0, 100, 5))
plt.bar(genderWithYear,empPercentage,color = col,width = 0.4)
plt.show()

#Fetching data using getDataByYrandCol function
total_Labour = getDataByYrandCol(2016,"Labor force,total")
female_Percentage = getDataByYrandCol(2016,"Labor force,female (%)")

#Deriving data useful for pie graph
no_Of_Female = getNumberofperson(female_Percentage,total_Labour)
no_Of_Male = total_Labour - no_Of_Female
#Getting number of person using getNumberofperson function
service_No_Of_Female = getNumberofperson(no_Of_Female ,service_Female2016)
service_No_Of_Male = getNumberofperson(no_Of_Male,service_Male2016)
total_In_Service = service_No_Of_Female + service_No_Of_Male
#Getting percentage using getpPercentage method
percent_Female = getpPercentage(service_No_Of_Female,total_In_Service)
percent_Male = getpPercentage(service_No_Of_Male,total_In_Service)

#Pie chart
plt.figure(figsize=(10,10))
myLabels = ["Female(2016)","Male(2016)"]
genderProportion= np.array([percent_Female,percent_Male])
myExplode = [0.05, 0]
plt.pie(genderProportion,labels=myLabels,shadow = True,explode= myExplode, autopct='%1.0f%%')
plt.title("Proportion of Male and female working in service sector(2016)(Uk)")
plt.legend()
plt.show()
















