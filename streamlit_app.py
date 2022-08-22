from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import calendar
import pyecharts
from pyecharts import options as opts
from pyecharts.charts import Bar,Calendar, Tab
import streamlit as st

st.set_page_config(page_title="FINANCIAL",
                   page_icon=":wink:",
                   layout="wide"
)

#df=pd.read_excel("Book2.xlsx",sheet_name='Book1')

#df1 - arkusz 2 dotyczacy planera rozdysponowania miesiecznych zarobkow
df1=pd.read_excel("Book2.xlsx",sheet_name='Book2')


#wykres treemap dla ostatniego miesiaca
dftree= df1[df1.Month == "08 August"]
#filtrowanie po pieniądzach
sales=dftree['Money']
ax2= px.treemap(dftree,path=['Account'],values=sales,title="Stan Kont Bankowych Dla Ostatniego Miesiąca:")
#ax2.show()

#wykres dla dwoch slupkow (nie dokończony)
#model_trans2=df1
#model_fuel2= model_trans2.groupby('Month')
#model_trans2 = model_trans2[model_trans2.Account == "Mbank"]
#model_trans2.plot(kind = 'bar', label = 'Wakajki', figsize = (4, 4))
#plt.xlabel('Month', fontsize = 16)
#plt.ylabel('Money', fontsize = 16)
#plt.show()

#wykres dla pojedynczych celow slupkowy (dziala)
cel_auto=df1[df1.Account == "Auto"]
cel_auto_mies= cel_auto.groupby('Month')['Money'].sum()
cel_auto_mies= pd.DataFrame(cel_auto_mies)
cel_auto_mies.columns = ['Money']
cel_auto_mies.sort_values(by=['Month'], inplace=True, ascending=True)
#usuwanie numerkow przed miesiacem
cel_auto_mies.index = [x.split()[1] for x in cel_auto_mies.index]
cel_auto_mies.index = cel_auto_mies.index.str.capitalize()
cel_auto_mies.plot(kind = 'bar', label = 'Wakajki', figsize = (4, 4))
plt.xlabel('Month', fontsize = 16)
plt.ylabel('Money', fontsize = 16)
#plt.show()

#proba donut diagram (test)
