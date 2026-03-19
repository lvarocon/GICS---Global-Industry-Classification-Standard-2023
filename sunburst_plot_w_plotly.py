# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:17:26 2026

@author: alvar
"""

import pandas as pd
import plotly.express as px

file_name = 'GICS - Global Industry Classification Standard.xlsx'
df = pd.read_excel(file_name)

path_cols = ['Sector', 'IndustryGroup', 'Industry', 'SubIndustry']

df_clean = df.dropna(subset=path_cols)

fig = px.sunburst(
    df_clean, 
    path=path_cols, 
    title='GICS Classification Sunburst Plot', 
    width=1000, 
    height=1000
)

fig.write_html('sunburst.html')