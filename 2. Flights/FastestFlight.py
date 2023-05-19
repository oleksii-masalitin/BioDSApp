import openpyxl as op

def getdata(ws):
    matrix = []
    for row in ws.values:
        l = []
        for value in row:
            l.append(value)
        matrix.append(l)
    return matrix

def difftime(time1, time2):
    time1, time2 = str(time1).split(':'), str(time2).split(':')
    time1 = [int(i) for i in time1]
    time2 = [int(i) for i in time2]
    difftime = (time2[0] - time1[0]) * 60 + (time2[1] - time1[1])
    if difftime < 0:
        difftime += 24*60
    return difftime

wb = op.load_workbook('Flights.xlsx')
city1 = 'Київ'
city2 = 'Париж'

airports = getdata(wb['Аеропорти'])
flights = getdata(wb['Рейси'])

airport_dict = {}
for row in airports[1:]:
    if row[2] not in airport_dict:
        airport_dict[row[2]] = []
    airport_dict[row[2]].append(row[0])

mintime = 10 ** 10
bestFligth = ''

if city1 not in airport_dict or city2 not in airport_dict:
    print('Потрібного вам рейсу не існує')
else:
    for row in flights[1:]:
        if row[0] in airport_dict[city1] and row[1] in airport_dict[city2]:
            flightTime = difftime(row[4], row[5])
            if flightTime < mintime:
                mintime = flightTime
                bestFligth = row[2]

if bestFligth == '':
    print('Потрібного вам рейсу не існує')
else:
    print('Найкоротший рейс – {}'.format(bestFligth))
