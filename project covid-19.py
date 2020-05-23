#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[35]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().system('pip install plotly')


# In[38]:


import plotly.offline as py
import plotly.express as px
#print(px.colors.sequential.Plasma)
##fig = px.colors.sequential.swatches()
#fig.show()


# In[37]:


fig = px.colors.cyclical.swatches_cyclical()
fig.show()

#fig = px.colors.cyclical.swatches()
#fig.show()


# In[4]:


down= pd.read_csv("C:\\Users\\Deepanshi\\Downloads\\covid_19_data.csv")
down


# In[5]:


down.columns


# In[6]:


py.init_notebook_mode(connected=True)


# In[40]:


corona = down.groupby(['ObservationDate', 'Country/Region'])['Confirm', 'Deaths', 'Recovered'].max()
corona = corona.reset_index()
corona['Date'] = pd.to_datetime(corona['ObservationDate'])
corona['Date'] = corona['Date'].dt.strftime('%m/%d/%Y')
corona['Active'] = corona['Confirm'] - corona['Recovered'] - corona['Deaths']
corona['Country'] =  corona['Country/Region']

fig = px.choropleth(corona, locations="Country", locationmode='country names', 
                     color="Confirm", hover_name="Country/Region",hover_data = [corona.Recovered,corona.Deaths,corona.Active],
                     # projection="natural earth",
                    
                     projection = ('orthographic'),
     #resolution_frame = '100',
                    
                    animation_frame="Date",width=950, height=980,
                     color_continuous_scale='Viridis',
                  
                
                     range_color=[1000,50000],
                     
                     title='VIRUS GLOBE')

fig.update(layout_coloraxis_showscale=True)
py.offline.iplot(fig)


# In[34]:


df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df, x="year", y="lifeExp", color='country')
fig.show()


# In[ ]:





# In[ ]:




