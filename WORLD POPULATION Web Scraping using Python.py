#!/usr/bin/env python
# coding: utf-8

# # NAME: ANIL KUMAR PODDAR

# In[1]:


# Installing Beautifulsoup
# pip install beautifulsoup4 - In CMD line
# !pip install beautifulsoup4 - In Jupyter cell
# OR
# %pip install beautifulsoup4 - In Jupyter cell


# In[2]:


# Installing Beautifulsoup
get_ipython().run_line_magic('pip', 'install beautifulsoup4')


# In[3]:


# Installing Requests
# pip install requests - In CMD line
# !pip install requests - In Jupyter cell
# OR
# %pip install requests - In Jupyter cell


# In[4]:


# Installing Requests
get_ipython().run_line_magic('pip', 'install requests')


# In[5]:


# Importing Matplotlib
import matplotlib.pyplot as plt
# plt is the alias name for pyplot
import pandas as pd
# pd is the alias for pandas
import seaborn as sns
# seaborn is aliased as sns
# Importing BeautifulSoup
from bs4 import BeautifulSoup
# Importing Requests
import requests

import warnings
warnings.filterwarnings("ignore")


# In[6]:


# URL for scrapping data
url = 'https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world/'


# In[7]:


response = requests.get(url) # Getting response form the website 
print(response) # If Respnse is 200, it is a valid response


# In[8]:


# parsing the response by using html.parser
soup = BeautifulSoup(response.text, 'html.parser') 
soup # Showing the Soup object


# In[9]:


# Getting data from the soup object
# As there are multiple 'td' tags we can use select method and than use square bracket to get the respective 'td' tag data, and than use .text method to extract the text data from the 'td' tag.
d1=soup.select('td')[0].text
d2=soup.select('td')[1].text
d3=soup.select('td')[2].text
d4=soup.select('td')[3].text
d5=soup.select('td')[4].text
d6=soup.select('td')[5].text
d7=soup.select('td')[6].text
d8=soup.select('td')[7].text
# Printing the first 8 data entries from the 'td' tag
d1,d2,d3,d4,d5,d6,d7,d8


# In[10]:


# As all the data is in 'td' tag ,using find_all method to get all the 'td' tags
data_iterator = soup.find_all('td')
data_iterator


# In[11]:


len(data_iterator) # Finging the length of data


# In[12]:


data=[] # Making an empty list 


# In[13]:


# Using for loop to itter through the data and using steps as 4, and appending the data in data list 
# Replacing the ',' in confirmed and deaths by '' (i.e removing he ',' from the numbers and converig the data type to int)
for i in range (0,len(data_iterator),5):
        Sr_no = soup.select('td')[i].text
        Country = soup.select('td')[i+1].text
        Population_2020 = soup.select('td')[i+2].text
        World_Share = soup.select('td')[i+3].text
        Land_Area = soup.select('td')[i+4].text
        data.append((
            Sr_no,Country,
            int(Population_2020.replace(',', '')),
            float(World_Share.replace('%', '')),
            int(Land_Area.replace(',', '')),
        ))


# In[14]:


data # Showing the Data collected from the website


# In[15]:


# create DataFrame using data by defining thecolumn headers
df = pd.DataFrame(data, columns =['Sr_no','Country','Population(2020)','World_Share(%)','Land_Area_Km²'])


# In[16]:


df.head() #Showing top 5 entries from the data


# In[17]:


# saving the dataframe
df.to_csv('WorldPopulation_2020_data.csv', index=False)


# In[18]:


df.columns


# ## Analyzing the Data

# A. Make a Scatter plot by using Seaborn and Matplotlib of 'Population(2020) vs Land_Area_Km²' and apply the following customization.
# - Make the Figure size (8,6)
# - Make a scatter plot such as x='Population(2020)',y='Land_Area_Km²',palette='Set1'
# - Add a title to the Plot with fontsize = 15 and color = purple as 'Population(2020) vs Land_Area_Km²'
# - Add Grid to the plot using grid() function
# - Also Show the plot

# In[19]:


plt.figure(figsize=(8,6)) # setting plot figure size
# Plotting a scatter plot and applying customization
sns.scatterplot(data=df,x='Population(2020)',y='Land_Area_Km²',palette='Set1')
# Setting title for the plot
plt.title('Population(2020) vs Land_Area_Km²')
plt.grid() # Showing grid for the plot 
plt.show()# Showing the plot


# In[20]:


# Top 5 Countries by Population(2020) , Using nlargest function of pandas
df_top_5=df.nlargest(n=5, columns=['Population(2020)'])
df_top_5


# B. Create a Line  plot of 'Country wise Population(2020)' of top 5 countries based on population and apply the Following customization to the plot.
# - Make a plot by setting figure size (10,6) using seaborn set() function.
# - Set the color palette for the plot using the set_palette() function as "tab10".
# - Set the style for the plot using the set_style() function as "darkgrid".
# - Set the context  for the plot using set_cotext() function with following customization ("paper", font_scale = 2, rc={"grid.linewidth": 0.5}).
# - Make a Bar plot using seaborn barplot() function setting x='Country',y='Population(2020)'.
# - Add the title to the plot as 'Country wise Population(2020)'.
# - Add X-label as 'Country' and Y-label as 'Country wise Population(2020)'
# - Make the Xticks rotate 45 degrees.
# - Show the plot using show() function of matplotlib

# In[21]:


# Setting the figure size for the plot
sns.set(rc={'figure.figsize':(10,6)})
# setting color palette for the plot
sns.set_palette("tab10")
# Setting background for the plot (setting grid style)
sns.set_style('darkgrid')
# setting figure style, font scale and grid line width for the plot
sns.set_context("paper", font_scale = 2, rc={"grid.linewidth": 0.5})
# Plotting a Bar plot
sns.barplot(data=df_top_5, x='Country',y='Population(2020)')
# Setting title for the plot
plt.title('Country wise Population(2020)')
plt.xlabel('Country') # setting x-label
plt.ylabel('Population(2020)')  # setting y-label
# Rotating x-label by 45 degrees
plt.xticks(rotation=45)
# Showing the plot
plt.show()


# C. Create a Line plot of 'Country vs Land_Area_Km² for top 5 countries by population' and apply the Following customization to the plot.
# - Make the Figure size (15,8)
# - Make line/markers color 'indigo'
# - Make line width as 2 and line style as '-.'
# - Add label as Land_Area_Km²
# - Add markers as 'o' with markersize = 10 
# - Add a title to the Plot with fontsize = 15 and color = purple
# - Add X-Label as Country & Y-Label as Land_Area_Km²
# - Add Grid to the plot using grid() function
# - Show the legend for the plot using legend() funct
# - Also Show the plot

# In[22]:


# Creating a line  plot and applying customization
plt.figure(figsize=(15,8)) # setting plt figure
# Customizing plot by setting line color, marker, label, markersize, linewidth(lw) and linestyle
plt.plot(df_top_5['Country'],df_top_5['Land_Area_Km²'],color='indigo',marker='o',
         label='Land_Area_Km²',markersize=10,lw=2,linestyle='-.')
plt.xlabel('Country') # Setting x-label
plt.ylabel('Land_Area_Km²') # Setting y-label
plt.legend() # Slowing Legend for the plot
# Setting title for the plot
plt.title('Country vs Land_Area_Km² for top 5 countries by population',fontsize=20,color='purple') 
plt.grid() # Showing grid for the plot 
plt.show() # Showing the plot


# In[ ]:




