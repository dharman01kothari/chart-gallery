# three_charts.py

#
# CHART 1 (PIE)
#
#import matplotlib.pyplot as plt 
import plotly
import plotly.graph_objs as go
import plotly.express as px
import plotly.graph_objects as pl

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

label=[]
for i in pie_data:
    label.append(i['company'])

mkt_share=[]
for i in pie_data:
    mkt_share.append(i['market_share'])

""" fig1, ax1 = plt.subplots()
ax1.pie(mkt_share, labels= labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')

plt.show()
 """

#print("----------------")
#print("GENERATING PIE CHART...")
#print(pie_data) # TODO: create a pie chart based on the pie_data

trace = go.Pie(labels=label, values = mkt_share)
plotly.offline.plot([trace], filename='pie_chart.html', auto_open= True)


#
# CHART 2 (LINE)
#

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

#print("----------------")
#print("GENERATING LINE GRAPH...")
#print(line_data) # TODO: create a line graph based on the line_data

x_axis=[]
for i in line_data:
    x_axis.append(i['date'])

price=[]
for i in line_data:
    price.append(i['stock_price_usd'])

plotly.offline.plot({
    "data": [go.Scatter(x=x_axis, y=price)],
    "layout": go.Layout(title="Stock Price")
}, auto_open=True)



#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

#print("----------------")
#print("GENERATING BAR CHART...")
#print(bar_data) # TODO: create a horizontal bar chart based on the bar_data

genre=[]
for i in bar_data:
    genre.append(i['genre'])

viewers=[]
for i in bar_data:
    viewers.append(i['viewers'])

#print(genre)

fig = pl.Figure(pl.Bar(
            x=viewers,
            y=genre, 
            orientation='h'))

fig.update_layout(title_text='Movies')

fig.show()