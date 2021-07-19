from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 
from tkinter import *
from tkinter import ttk

root = Tk()


url = 'https://www.pro-football-reference.com/years/2020/passing.htm#passing::pass_cmp'
html = urlopen(url)
passing_stats = BeautifulSoup(html, features="html.parser")

column_headers = passing_stats.findAll('tr')[0]
column_headers = [i.getText() for i in column_headers.findAll('th')]
rows = passing_stats.findAll('tr')[1:]



qb_stats = []
for i in range(len(rows)):
    qb_stats.append([col.getText() for col in rows[i].findAll('td')])


data = pd.DataFrame(qb_stats, columns=column_headers[1:])
new_column = data.columns.values
new_column[-6] = 'Yds_Sack'
data.columns = new_column
categories = ['Cmp%', 'Yds', 'TD', 'Int', 'Y/A', 'Rate']
data_radar = data[['Player', 'Tm'] + categories]


for i in categories:
    data_radar[i] = pd.to_numeric(data[i])

data_radar['Player'] = data_radar['Player'].str.replace('*', '')
data_radar['Player'] = data_radar['Player'].str.replace('+', '')

data_radar_filtered = data_radar[data_radar['Yds'] > 1500].sort_values(by='TD', ascending=True)
data_radar_filtered_yds = data_radar[data_radar['Yds'] > 1500].sort_values(by='Yds', ascending=True)
plt.style.use('ggplot')


def tot_yards():
    fig, ax = plt.subplots(figsize=(15,15))

    player = data_radar_filtered_yds['Player']
    x = np.arange(len(player))
    y = data_radar_filtered_yds['Yds']
    width = .4
    dx = data_radar_filtered_yds['Yds'].max() / 100

    plt.title("Total Yards (>1,500 yards)")
    ax.barh(x, y, width, label="Passing Yards")
    ax.set_xlabel("Passing Yards")
    ax.set_ylabel("Quarterback")
    ax.set_yticks(x)
    ax.set_yticklabels(player)
    
    for i, (value, name) in enumerate(zip(data_radar_filtered_yds['Yds'], data_radar_filtered_yds['Player'])):
        ax.text(value+dx, i, f'{value:,.0f}', ha='left', va='center', fontsize=9) 

    plt.show()


def td_int():

    fig, ax = plt.subplots(figsize=(15,15))

    player = data_radar_filtered['Player']
    x = np.arange(len(player))
    y = data_radar_filtered['TD']
    z = data_radar_filtered['Int']
    width = .4
    dx = data_radar_filtered['TD'].max() / 100
    dy = data_radar_filtered['Int'].max() / 100
    
    plt.title("Total TD/INT for all Quarterbacks" + '\n' + "(QBs Over 1,500 Passing Yards)")
    ax.barh(x + width/2, y, width, label='Touchdowns')
    ax.barh(x - width/2, z, width, label='Interceptions')
    ax.set_xlabel("TD/INT")
    ax.set_ylabel("Quarterbacks" + '\n' + "(>1,500 yards)")
    ax.legend(loc='lower right')
    ax.set_yticks(x)
    ax.set_yticklabels(player)
    
    for i, (value, turnover, name) in enumerate(zip(data_radar_filtered['TD'], data_radar_filtered['Int'], data_radar_filtered['Player'])):
        ax.text(value+dx, i, f'{value:,.0f}', ha='left', va='bottom', fontsize=9)
        ax.text(turnover+dy, i, f'{turnover:,.0f}', ha='left', va='top', fontsize=9)
    plt.show()

style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')])

td = ttk.Button(root, text="Passing TD's", style="C.TButton", command=td_int)
td.place(relx=0.5, rely=0.0, anchor=N)

yrds = ttk.Button(root, text="Passing Yards", style="C.TButton", command=tot_yards)
yrds.place(relx=0.5, rely=0.2, anchor=N)

root.mainloop()
