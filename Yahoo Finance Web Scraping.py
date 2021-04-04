import csv
from io import StringIO
import requests

outfile = open("FordMotorCompany.csv", "w", newline='')
writer = csv.writer(outfile)

outfile2 = open("HondaMotorsCompany.csv", "w", newline='')
writer2 = csv.writer(outfile2)

outfile3 = open("MarutiSuzukiIndiaLimited.csv", "w", newline='')
writer3 = csv.writer(outfile3)

outfile4 = open("TeslaMotors.csv", "w", newline='')
writer4 = csv.writer(outfile4)

outfile5 = open("ToyotaMotorCorporation.csv", "w", newline='')
writer5 = csv.writer(outfile5)

stock1 = 'F'
stock2 = 'HMC'
stock3 = 'MARUTI.NS'
stock4 = 'TSLA'
stock5 = 'TM'

stock_url = 'https://query1.finance.yahoo.com/v7/finance/download/{}'
params = {
    'range': '5y',
    'interval': '1d',
    'events': 'history',
    'includeAdjustedClose': 'true'
}

# Ford Motor Company
response = requests.get(stock_url.format(stock1), params=params)
file = StringIO(response.text)
reader = csv.reader(file)
data = list(reader)
stock_return_percent_list = []
dates = []
for row in data[1:]:
    dates.append(row[0])
    if row[1] == "null":
        stock_return_percent_list.append("null")
    else:
        stock_difference = float(row[4]) - float(row[1])
        stock_return = (stock_difference / float(row[1]))
        stock_return_percent = float(stock_return) * 100
        stock_return_percent_list.append(float(stock_return_percent))

a = list(zip(dates, stock_return_percent_list))

with open('FordMotorCompany.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    headers = ['Date', 'Return']
    writer.writerow(headers)
    for row in a:
        writer.writerow(row)
outfile.close()

# Honda Motors Company Limited
response2 = requests.get(stock_url.format(stock2), params=params)
file2 = StringIO(response2.text)
reader2 = csv.reader(file2)
data2 = list(reader2)
stock_return_percent_list_2 = []
dates_2 = []
for row in data2[1:]:
    dates_2.append(row[0])
    if row[1] == "null":
        stock_return_percent_list_2.append("null")
    else:
        stock_difference_2 = float(row[4]) - float(row[1])
        stock_return_2 = (stock_difference_2 / float(row[1]))
        stock_return_percent_2 = float(stock_return_2) * 100
        stock_return_percent_list_2.append(float(stock_return_percent_2))

a_2 = list(zip(dates_2, stock_return_percent_list_2))

with open('HondaMotorsCompany.csv', 'w', newline='') as file2:
    writer2 = csv.writer(file2)
    headers2 = ['Date', 'Return']
    writer2.writerow(headers2)
    for row in a_2:
        writer2.writerow(row)
outfile2.close()

# Ford Motor Company
response3 = requests.get(stock_url.format(stock3), params=params)
file3 = StringIO(response3.text)
reader3 = csv.reader(file3)
data3 = list(reader3)
stock_return_percent_list_3 = []
dates_3 = []
for row in data3[1:]:
    dates_3.append(row[0])
    if row[1] == "null":
        stock_return_percent_list_3.append("null")
    else:
        stock_difference_3 = float(row[4]) - float(row[1])
        stock_return_3 = (stock_difference_3 / float(row[1]))
        stock_return_percent_3 = float(stock_return_3) * 100
        stock_return_percent_list_3.append(float(stock_return_percent_3))

a_3 = list(zip(dates_3, stock_return_percent_list_3))

with open('MarutiSuzukiIndiaLimited.csv', 'w', newline='') as file3:
    writer3 = csv.writer(file3)
    headers3 = ['Date', 'Return']
    writer3.writerow(headers3)
    for row in a_3:
        writer3.writerow(row)
outfile3.close()

# Tesla Motors
response4 = requests.get(stock_url.format(stock4), params=params)
file4 = StringIO(response4.text)
reader4 = csv.reader(file4)
data4 = list(reader4)
stock_return_percent_list_4 = []
dates_4 = []
for row in data4[1:]:
    dates_4.append(row[0])
    if row[1] == "null":
        stock_return_percent_list_4.append("null")
    else:
        stock_difference_4 = float(row[4]) - float(row[1])
        stock_return_4 = (stock_difference_4 / float(row[1]))
        stock_return_percent_4 = float(stock_return_4) * 100
        stock_return_percent_list_4.append(float(stock_return_percent_4))

a_4 = list(zip(dates_4, stock_return_percent_list_4))

with open('TeslaMotors.csv', 'w', newline='') as file4:
    writer4 = csv.writer(file4)
    headers4 = ['Date', 'Return']
    writer4.writerow(headers4)
    for row in a_4:
        writer4.writerow(row)
outfile4.close()

# Toyota Motor Corporation
response5 = requests.get(stock_url.format(stock5), params=params)
file5 = StringIO(response5.text)
reader5 = csv.reader(file5)
data5 = list(reader5)
stock_return_percent_list_5 = []
dates_5 = []
for row in data5[1:]:
    dates_5.append(row[0])
    if row[1] == "null":
        stock_return_percent_list_5.append("null")
    else:
        stock_difference_5 = float(row[4]) - float(row[1])
        stock_return_5 = (stock_difference_5 / float(row[1]))
        stock_return_percent_5 = float(stock_return_5) * 100
        stock_return_percent_list_5.append(float(stock_return_percent_5))

a_5 = list(zip(dates_5, stock_return_percent_list_5))

with open('ToyotaMotorCorporation.csv', 'w', newline='') as file5:
    writer5 = csv.writer(file5)
    headers5 = ['Date', 'Return']
    writer5.writerow(headers5)
    for row in a_5:
        writer5.writerow(row)
outfile5.close()
