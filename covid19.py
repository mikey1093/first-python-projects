import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from datetime import datetime
from datetime import date
from datetime import timedelta
from random import randint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv


root = Tk()
root.title("COVID-19 Data")
root.geometry("400x196")

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv"
url_1 = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
df = pd.read_csv(url)
df.columns = ['date', 'state', 'fips', 'cases', 'deaths', 'confirmed_cases', 'confirmed_deaths', 'probable_cases', 'probable_deaths']
df1 = pd.read_csv(url_1)

pop = [['Alabama', 4903185], ['Alaska', 731545], ['Arizona', 7278717], ['Arkansas', 3017804], ['California', 39512223], ['Colorado', 5758736], ['Connecticut', 3565287], ['Delaware', 973764], ['District Of Columbia', 705749], ['Florida', 21477737], ['Georgia', 10617423], ['Guam', 167294], ['Hawaii', 1415872], ['Idaho', 1787065], ['Illinois', 12671821], ['Indiana', 6732219], ['Iowa', 3155070], ['Kansas', 2913314], ['Kentucky', 4467673], ['Louisiana', 4648794], ['Maine', 1344212], ['Maryland', 6045680], ['Massachusetts', 6892503], ['Michigan', 9986857], ['Minnesota', 5639632], ['Mississippi', 2976149], ['Missouri', 6137428], ['Montana', 1068778], ['Nebraska', 1934408], ['Nevada', 3080156], ['New Hampshire', 1359711], ['New Jersey', 8882190], ['New Mexico', 2096829], ['New York', 19453561], ['North Carolina', 10488084], ['North Dakota', 762062], ['Northern Mariana Islands', 57559], ['Ohio', 11689100], ['Oklahoma', 3956971], ['Oregon', 4217737], ['Pennsylvania', 12801989], ['Puerto Rico', 3193694], ['Rhode Island', 1059361], ['South Carolina', 5148714], ['South Dakota', 884659], ['Tennessee', 6829174], ['Texas', 28995881], ['Utah', 3205958], ['Vermont', 623989], ['Virginia', 8535519], ['Virgin Islands', 104578], ['Washington', 7614893], ['West Virginia', 1792147], ['Wisconsin', 5822434], ['Wyoming', 578759]]
popdf = pd.DataFrame(pop, columns=['state', 'population'])
popdf.drop(['state'], axis=1, inplace=True)
frames = [df, popdf]
result = pd.concat(frames, ignore_index=True, axis=1)
result.columns = ['date', 'state', 'fips', 'cases', 'deaths', 'confirmed_cases', 'confirmed_deaths', 'probable_cases', 'probable_deaths', 'population']
result["Per Capita"] = result["cases"].div(other = 100000)
print(result)


e = Entry(root, width=35, borderwidth=5)  
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
plt.style.use('ggplot')

def error():
    response = messagebox.showerror("Input Error", "Please Enter a Valid State")

def getText():
    top = Tk()
    current = e.get()
    current_date = str(date.today())
    df = pd.read_csv(url)
    if current == 'Alabama' or current == 'alabama' or current == 'AL':
        label_state = Label(top, text=df.iloc[0,3:5]).grid(row=0, column=0)
    if current == 'Alaska' or current == 'alaska' or current == 'AK':
        label_state = Label(top, text=df.iloc[1,3:5]).grid(row=0, column=0)
    if current == 'Arizona' or current == 'arizona' or current == 'AZ':
        label_state = Label(top, text=df.iloc[2,3:5]).grid(row=0, column=0)
    if current == 'Arkansas' or current == 'arkansas' or current == 'AR':
        label_state = Label(top, text=df.iloc[3,3:5]).grid(row=0, column=0)
    if current == 'California' or current == 'california' or current == 'CA':
        label_state = Label(top, text=df.iloc[4,3:5]).grid(row=0, column=0)
    if current == 'Colorado' or current == 'colorado' or current == 'CO':
        label_state = Label(top, text=df.iloc[5,3:5]).grid(row=0, column=0)
    if current == 'Connecticut' or current == 'connecticut' or current == 'CT':
        label_state = Label(top, text=df.iloc[6,3:5]).grid(row=0, column=0)
    if current == 'Delaware' or current == 'delaware' or current == 'DE':
        label_state = Label(top, text=df.iloc[7,3:5]).grid(row=0, column=0)
    if current == 'District of Columbia' or current == 'washington DC' or current == 'DC' or current == 'washington dc' or current == 'dc':
        label_state = Label(top, text=df.iloc[8,3:5]).grid(row=0, column=0)
    if current == 'Florida' or current == 'florida' or current == 'FL':
        label_state = Label(top, text=df.iloc[9,3:5]).grid(row=0, column=0)
    if current == 'Georgia' or current == 'georgia' or current == 'GA':
        label_state = Label(top, text=df.iloc[10,3:5]).grid(row=0, column=0)
    if current == 'Guam' or current == 'guam' or current == 'GU':
        label_state = Label(top, text=df.iloc[11,3:5]).grid(row=0, column=0)
    if current == 'Hawaii' or current == 'hawaii' or current == 'HI':
        label_state = Label(top, text=df.iloc[12,3:5]).grid(row=0, column=0)
    if current == 'Idaho' or current == 'idaho' or current == 'ID':
        label_state = Label(top, text=df.iloc[13,3:5]).grid(row=0, column=0)
    if current == 'Illinois' or current == 'illinois' or current == 'IL':
        label_state = Label(top, text=df.iloc[14,3:5]).grid(row=0, column=0)
    if current == 'Indiana' or current == 'indiana' or current == 'IN':
        label_state = Label(top, text=df.iloc[15,3:5]).grid(row=0, column=0)
    if current == 'Iowa' or current == 'iowa' or current == 'IA':
        label_state = Label(top, text=df.iloc[16,3:5]).grid(row=0, column=0)
    if current == 'Kansas' or current == 'kansas' or current == 'KS':
        label_state = Label(top, text=df.iloc[17,3:5]).grid(row=0, column=0)
    if current == 'Kentucky' or current == 'kentucky' or current == 'KY':
        label_state = Label(top, text=df.iloc[18,3:5]).grid(row=0, column=0)
    if current == 'Louisiana' or current == 'louisiana' or current == 'LA':
        label_state = Label(top, text=df.iloc[19,3:5]).grid(row=0, column=0)
    if current == 'Maine' or current == 'maine' or current == 'ME':
        label_state = Label(top, text=df.iloc[20,3:5]).grid(row=0, column=0)
    if current == 'Maryland' or current == 'maryland' or current == 'MD':
        label_state = Label(top, text=df.iloc[21,3:5]).grid(row=0, column=0)
    if current == 'Massachusetts' or current == 'massachusetts' or current == 'MA':
        label_state = Label(top, text=df.iloc[22,3:5]).grid(row=0, column=0)
    if current == 'Michigan' or current == 'michigan' or current == 'MI':
        label_state = Label(top, text=df.iloc[23,3:5]).grid(row=0, column=0)
    if current == 'Minnesota' or current == 'minnesota' or current == 'MN':
        label_state = Label(top, text=df.iloc[24,3:5]).grid(row=0, column=0)
    if current == 'Mississippi' or current == 'mississippi' or current == 'MS':
        label_state = Label(top, text=df.iloc[25,3:5]).grid(row=0, column=0)
    if current == 'Missouri' or current == 'missouri' or current == 'MO':
        label_state = Label(top, text=df.iloc[26,3:5]).grid(row=0, column=0)
    if current == 'Montana' or current == 'montana' or current == 'MO':
        label_state = Label(top, text=df.iloc[27,3:5]).grid(row=0, column=0)
    if current == 'Nebraska' or current == 'nebraska' or current == 'NE':
        label_state = Label(top, text=df.iloc[28,3:5]).grid(row=0, column=0)
    if current == 'Nevada' or current == 'nevada' or current == 'NV':
        label_state = Label(top, text=df.iloc[29,3:5]).grid(row=0, column=0)
    if current == 'New Hampshire' or current == 'new hampshire' or current == 'NH':
        label_state = Label(top, text=df.iloc[30,3:5]).grid(row=0, column=0)
    if current == 'New Jersey' or current == 'new jersey' or current == 'NJ':
        label_state = Label(top, text=df.iloc[31,3:5]).grid(row=0, column=0)
    if current == 'New Mexico' or current == 'new mexico' or current == 'NM':
        label_state = Label(top, text=df.iloc[32,3:5]).grid(row=0, column=0)
    if current == 'New York' or current == 'new york' or current == 'NY':
        label_state = Label(top, text=df.iloc[33,3:5]).grid(row=0, column=0)
    if current == 'North Carolina' or current == 'north carolina' or current == 'NC':
        label_state = Label(top, text=df.iloc[34,3:5]).grid(row=0, column=0)
    if current == 'North Dakota' or current == 'north dakota' or current == 'ND':
        label_state = Label(top, text=df.iloc[35,3:5]).grid(row=0, column=0)
    if current == 'Northern Mariana Islands' or current == 'Mariana Islands' or current == 'north mariana islands' or current == 'MP':
        label_state = Label(top, text=df.iloc[36,3:5]).grid(row=0, column=0)
    if current == 'Ohio' or current == 'ohio' or current == 'OH':
        label_state = Label(top, text=df.iloc[37,3:5]).grid(row=0, column=0)
    if current == 'Oklahoma' or current == 'oklahoma' or current == 'OK':
        label_state = Label(top, text=df.iloc[38,3:5]).grid(row=0, column=0)
    if current == 'Oregon' or current == 'oregon' or current == 'OR':
        label_state = Label(top, text=df.iloc[39,3:5]).grid(row=0, column=0)
    if current == 'Pennsylvania' or current == 'pennsylvania' or current == 'PA':
        label_state = Label(top, text=df.iloc[40,3:5]).grid(row=0, column=0)
    if current == 'Puerto Rico' or current == 'puerto rico' or current == 'PR':
        label_state = Label(top, text=df.iloc[41,3:5]).grid(row=0, column=0)
    if current == 'Rhode Island' or current == 'rhode island' or current == 'RI':
        label_state = Label(top, text=df.iloc[42,3:5]).grid(row=0, column=0)
    if current == 'South Carolina' or current == 'south carolina' or current == 'SC':
        label_state = Label(top, text=df.iloc[43,3:5]).grid(row=0, column=0)
    if current == 'South Dakota' or current == 'south dakota' or current == 'SD':
        label_state = Label(top, text=df.iloc[44,3:5]).grid(row=0, column=0)
    if current == 'Tennessee' or current == 'tennessee' or current == 'TN':
        label_state = Label(top, text=df.iloc[45,3:5]).grid(row=0, column=0)
    if current == 'Texas' or current == 'texas' or current == 'TX':
        label_state = Label(top, text=df.iloc[46,3:5]).grid(row=0, column=0)
    if current == 'Utah' or current == 'utah' or current == 'UT':
        label_state = Label(top, text=df.iloc[47,3:5]).grid(row=0, column=0)
    if current == 'Vermont' or current == 'vermont' or current == 'VT':
        label_state = Label(top, text=df.iloc[48,3:5]).grid(row=0, column=0)
    if current == 'Virginia' or current == 'virginia' or current == 'VA':
        label_state = Label(top, text=df.iloc[49,3:5]).grid(row=0, column=0)
    if current == 'Virgin Islands' or current == 'virgin islands' or current == 'VI':
        label_state = Label(top, text=df.iloc[50,3:5]).grid(row=0, column=0)
    if current == 'Washington' or current == 'washington' or current == 'WA':
        label_state = Label(top, text=df.iloc[51,3:5]).grid(row=0, column=0)
    if current == 'West Virginia' or current == 'west virginia' or current == 'WV':
        label_state = Label(top, text=df.iloc[52,3:5]).grid(row=0, column=0)
    if current == 'Wisconsin' or current == 'wisconsin' or current == 'WI':
        label_state = Label(top, text=df.iloc[53,3:5]).grid(row=0, column=0)
    if current == 'Wyoming' or current == 'wyoming' or current == 'WY':
        label_state = Label(top, text=df.iloc[54,3:5]).grid(row=0, column=0)

def totals(df, x_dim, y_dim, z_dim):
    current_date = str(date.today())
    dff = df[df['date'].eq(current_date)].sort_values(by='cases', ascending=False)
    dfff = df[df['date'].eq(current_date)].sort_values(by='deaths', ascending=False)
    states = dff[x_dim]
    x = np.arange(len(states))
    y = dff[y_dim]
    z = dff[z_dim]
    dx = dff['cases'].max() / 100
    dy = dff['deaths'].max() / 100
    width = .4
    fig, ax = plt.subplots(figsize=(40,10))
    plt.title("Total COVID cases as of " + str(date.today()))
    ax.set_xlabel('Number of Cases (x 10^6)')
    ax.set_ylabel('States')
    ax.barh(x + width/2, y, width, label='cases')
    ax.barh(x - width/2, z, width, label='deaths')
    ax.set_yticks(x)
    ax.set_yticklabels(states)
    leg = ax.legend(loc='upper right')
    for i, (value, name, deaths) in enumerate(zip(dff['cases'], dff['state'], dff['deaths'])):
        ax.text(value+dx, i, f'{value:,.0f}', size=10, ha='left', va='bottom', fontsize=6)
        ax.text(deaths+dy, i, f'{deaths:,.0f}', ha='left', va='top', fontsize=6)
    plt.show()

def deaths(df, x_dim, y_dim):
    current_date = str(date.today())
    dff = df[df['date'].eq(current_date)].sort_values(by='deaths', ascending=False)
    x = dff[x_dim]
    y = dff[y_dim]
    fig, ax = plt.subplots(figsize=(15,10))
    plt.title("Total COVID cases as of " + str(date.today()))
    ax.set_xlabel('Number of Deaths')
    ax.set_ylabel('States')
    dx = dff['deaths'].max() / 100
    ax.barh(x, y)
    for i, (value, name) in enumerate(zip(dff['deaths'], dff['state'])):
        ax.text(value+dx, i, f'{value:,.0f}', size=10, ha='left', va='center')
    plt.show()

def capita(df, x_dim, y_dim):
    current_date = str(date.today())
    resultdf = result[result['date'].eq(current_date)].sort_values(by='Per Capita', ascending=False)
    x = resultdf[x_dim]
    y = resultdf[y_dim]
    dx = resultdf['Per Capita'].max() / 100
    fig, ax = plt.subplots(figsize=(15,10))
    plt.title("COVID Cases Per Captia as of " + str(date.today()))
    ax.set_xlabel('Cases Per 100,000 people')
    ax.set_ylabel('States')
    col = []
    for i in y:
        if i >= 5.1:
            col.append('red')
        if 2.6 <= i <= 5:
            col.append('orange')
        if .5 <= i <= 2.5:
            col.append('yellow')
        if i < .5:
            col.append('green')
    ax.barh(x, y, color = col)
    for i, (value, name) in enumerate(zip(resultdf['Per Capita'], resultdf['state'])):
        ax.text(value+dx, i, float(f'{value:,.0f}'), size=10, ha='left', va='center')
    plt.show()    
    
style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')])

text = ttk.Button(root, text="Get Data", style="C.TButton", command=getText).grid(row=1, column=0, columnspan=2, padx=10, sticky='NEWS')

total = ttk.Button(root, text='Total Cases by State', style="C.TButton", command=lambda: totals(df, 'state', 'cases', 'deaths'))
total.grid(row=2, column=0, columnspan=2, padx=10, pady=3, sticky='NEWS')

death = ttk.Button(root, text='Total Deaths by State', style="C.TButton", command=lambda: deaths(df, 'state','deaths'))
death.grid(row=3, column=0, columnspan=2, padx=10, pady=3, sticky='NEWS')

per_C = ttk.Button(root, text='Cases Per Capita', style="C.TButton", command=lambda: capita(result, 'state', 'Per Capita'))
per_C.grid(row=4, column=0, columnspan=2, padx=10, pady=3, sticky='NEWS')


root.mainloop()
