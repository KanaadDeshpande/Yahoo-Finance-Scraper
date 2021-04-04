# importing the required module
import matplotlib.pyplot as plt
import csv
from io import StringIO
import requests

stock = 'RELIANCE.NS'
stock_url = 'https://query1.finance.yahoo.com/v7/finance/download/{}'
params = {
    'range': '5y',
    'interval': '1mo',
    'events': 'history',
    'includeAdjustedClose': 'true'
}
# Reliance Industries Pvt. Ltd.

# Request the required data
response = requests.get(stock_url.format(stock), params=params)
file = StringIO(response.text)
reader = csv.reader(file)
data = list(reader)

# Extract dates and returns from the data
stock_return_percent_list = []
dates = []
for row in data[1:]:
    try:
        dates.append(row[0])
        stock_difference = float(row[4]) - float(row[1])
        stock_return = (stock_difference / float(row[1]))
        stock_return_percent = float(stock_return) * 100
        stock_return_percent_list.append(float(stock_return_percent))
    except:
        print("Value not found")

x = dates
y = stock_return_percent_list

# Plotting the points
plt.plot(x, y)
plt.xticks(rotation=45)
plt.yticks(rotation=45)

# Naming the x axis
plt.xlabel('Dates')
# Naming the y axis
plt.ylabel('Stock Returns')

# Giving a title to my graph
plt.title('Reliance Stock Returns')

# Function to show the plot
plt.show()
