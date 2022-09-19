#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()


# In[3]:


d1= today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today()- timedelta(days=720)
d2= d2.strftime("%Y-%m-%d")
start_date = d2


# In[7]:


data = yf.download('AAPL', start= start_date, 
                  end=end_date, progress=False)
print(data.head())


# In[10]:


import plotly.express as px


# In[11]:


figure = px.line(data, x = data.index, 
                 y = "Close", 
                 title = "Time Series Analysis (Line Plot)")
figure.show()


# In[13]:


import plotly.graph_objects as go
figure = go.Figure(data=[go.Candlestick(x= data.index,
                                       open= data["Open"],
                                       high= data["High"],
                                      low= data["Low"],
                                       close= data["Close"])])
figure.update_layout(title = "Time Series Analysis (Candlestick Chart)",
                    xaxis_rangeslider_visible = False)
figure.show()


# In[14]:


figure = px.bar(data, x = data.index,
               y= "Close",
               title = "Time Series Analysis (Bar Plot)" )
figure.show()


# ###Analyzing stock prices between the period of two specific dates

# In[16]:


figure = px.line(data, x= data.index,
                y="Close",
                range_x= ['2021-07-01','2021-12-31'],
                title = "Time Series Analysis (Custom Date Range)")
figure.show()


# ### Interactive candlestick chart where you can select time intervals in the output itself

# In[19]:


figure  = go.Figure(data =[go.Candlestick(x=data.index,
                                         open = data["Open"],
                                         high=data["High"],
                                         low= data["Low"],
                                          close=data["Close"])])
figure.update_layout(title = "Time Series Analysis (Candlestick Chart with Buttons and Slider)")
figure.update_xaxes(
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = "1m", step = "month", stepmode = "backward"),
            dict(count = 6, label = "6m", step = "month", stepmode = "backward"),
            dict(count = 1, label = "YTD", step = "year", stepmode = "todate"),
            dict(count = 1, label = "1y", step = "year", stepmode = "backward"),
            dict(step = "all")
        ])
    )
)
figure.show()


# In[ ]:




