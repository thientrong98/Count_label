# Program extracting first column 
import xlrd 
from collections import Counter
import plotly.graph_objects as go
loc = ("./Dataset_translate.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
# sheet.cell_value(1, 1) 

list = []
for i in range(sheet.nrows-1): 
    list.append(sheet.cell_value(i+1, 2))

listKey = []
listValue = []
for i in Counter(list).values():
    listValue.append(i)
for i in Counter(list).keys():
    listKey.append(i)

fig = go.Figure(
    data=[go.Bar(x=listKey,y=listValue)],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.DataFrame([['g1','c1',10],['g1','c2',12],['g1','c3',13],['g2','c1',8],
#                    ['g2','c2',10],['g2','c3',12]],columns=['group','column','val'])

# df.pivot("column", "group", "val").plot(kind='bar')

# plt.show()
